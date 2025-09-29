#!/usr/bin/env python3
"""
GIACONVERT Web Application Backend
FastAPI server that provides REST API endpoints for Word to HTML conversion.
"""

import os
import sys
import json
import uuid
import asyncio
import tempfile
import traceback
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict, Any
from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, UploadFile, File, Form, BackgroundTasks
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Import our universal converter
from giaconvert_universal import UniversalDocumentConverter

# Global variables for tracking conversions
active_conversions = {}
conversion_results = {}

# Conversion modes mapping (using the universal converter for all modes)
CONVERTER_CLASSES = {
    'basic': UniversalDocumentConverter,
    'enhanced': UniversalDocumentConverter,
    'complete': UniversalDocumentConverter
}

# Data models
class ConversionRequest(BaseModel):
    files: List[str]  # File paths or upload IDs
    mode: str  # 'basic', 'enhanced', 'complete'
    output_option: str  # 'beside', 'mirrored', 'single_folder'
    destination_path: Optional[str] = None  # For mirrored/single_folder options

class ConversionStatus(BaseModel):
    conversion_id: str
    status: str  # 'pending', 'processing', 'completed', 'failed'
    progress: float  # 0.0 to 1.0
    current_file: Optional[str] = None
    completed_files: int = 0
    total_files: int = 0
    results: List[Dict[str, Any]] = []
    errors: List[Dict[str, Any]] = []
    start_time: Optional[str] = None
    end_time: Optional[str] = None

class FileUploadResponse(BaseModel):
    upload_id: str
    filename: str
    size: int
    path: str

# Error handling
class GiaconvertError(Exception):
    def __init__(self, error_code: str, message: str, details: Dict[str, Any] = None):
        self.error_code = error_code
        self.message = message
        self.details = details or {}
        super().__init__(message)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan management"""
    # Startup
    print("🚀 GIACONVERT Web Application starting...")
    
    # Create temp directory for uploads
    upload_dir = Path(tempfile.gettempdir()) / "giaconvert_uploads"
    upload_dir.mkdir(exist_ok=True)
    app.state.upload_dir = upload_dir
    
    print(f"📁 Upload directory: {upload_dir}")
    print("✅ Server ready!")
    
    yield
    
    # Shutdown
    print("🛑 GIACONVERT Web Application shutting down...")
    
    # Cleanup temp files
    try:
        import shutil
        if upload_dir.exists():
            shutil.rmtree(upload_dir)
            print("🧹 Temporary files cleaned up")
    except Exception as e:
        print(f"⚠️  Error cleaning up temp files: {e}")

# Create FastAPI app
app = FastAPI(
    title="GIACONVERT Web API",
    description="Word to HTML conversion service with web interface",
    version="1.0.0",
    lifespan=lifespan
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
static_dir = Path(__file__).parent / "web"
app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

# API Routes

@app.get("/")
async def root():
    """Serve the main application page"""
    static_dir = Path(__file__).parent / "web"
    index_file = static_dir / "index.html"
    
    if index_file.exists():
        return FileResponse(str(index_file))
    else:
        return JSONResponse({
            "message": "GIACONVERT Web API",
            "version": "1.0.0",
            "status": "running",
            "endpoints": {
                "upload": "/api/upload",
                "convert": "/api/convert",
                "status": "/api/status/{conversion_id}",
                "download": "/api/download/{file_id}"
            }
        })

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/api/modes")
async def get_conversion_modes():
    """Get available conversion modes with descriptions"""
    return {
        "modes": {
            "basic": {
                "name": "Basic",
                "description": "Convert text and tables only",
                "features": ["Text formatting", "Tables", "Fast conversion"]
            },
            "enhanced": {
                "name": "Enhanced",
                "description": "Includes images with optimization",
                "features": ["Text formatting", "Tables", "Images", "Image optimization"]
            },
            "complete": {
                "name": "Complete", 
                "description": "Full document with headers and footers",
                "features": ["Text formatting", "Tables", "Images", "Headers/Footers", "Page layout"]
            }
        }
    }

@app.post("/api/upload", response_model=List[FileUploadResponse])
async def upload_files(files: List[UploadFile] = File(...)):
    """Upload Word documents for conversion"""
    upload_responses = []
    
    for file in files:
        if not file.filename.lower().endswith('.docx'):
            raise HTTPException(
                status_code=400,
                detail=f"File {file.filename} is not a Word document (.docx)"
            )
        
        # Generate upload ID and save file
        upload_id = str(uuid.uuid4())
        file_path = app.state.upload_dir / f"{upload_id}_{file.filename}"
        
        try:
            content = await file.read()
            file_path.write_bytes(content)
            
            upload_responses.append(FileUploadResponse(
                upload_id=upload_id,
                filename=file.filename,
                size=len(content),
                path=str(file_path)
            ))
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to save {file.filename}: {str(e)}"
            )
    
    return upload_responses

@app.post("/api/convert")
async def start_conversion(
    request: ConversionRequest,
    background_tasks: BackgroundTasks
):
    """Start document conversion process"""
    
    # Validate conversion mode
    if request.mode not in CONVERTER_CLASSES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid conversion mode: {request.mode}"
        )
    
    # Validate output option
    if request.output_option not in ['beside', 'mirrored', 'single_folder']:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid output option: {request.output_option}"
        )
    
    # Validate destination for mirrored/single_folder options
    if request.output_option in ['mirrored', 'single_folder'] and not request.destination_path:
        raise HTTPException(
            status_code=400,
            detail=f"Destination path required for {request.output_option} output option"
        )
    
    # Generate conversion ID
    conversion_id = str(uuid.uuid4())
    
    # Initialize conversion status
    status = ConversionStatus(
        conversion_id=conversion_id,
        status='pending',
        progress=0.0,
        total_files=len(request.files),
        start_time=datetime.now().isoformat()
    )
    
    active_conversions[conversion_id] = status
    
    # Start background conversion
    background_tasks.add_task(
        process_conversion,
        conversion_id,
        request
    )
    
    return {"conversion_id": conversion_id, "status": "started"}

@app.get("/api/status/{conversion_id}", response_model=ConversionStatus)
async def get_conversion_status(conversion_id: str):
    """Get conversion progress and status"""
    
    if conversion_id not in active_conversions:
        raise HTTPException(
            status_code=404,
            detail="Conversion not found"
        )
    
    return active_conversions[conversion_id]

@app.get("/api/download/{file_id}")
async def download_file(file_id: str):
    """Download converted HTML file"""
    
    # In a real implementation, you'd map file_id to actual file paths
    # For now, this is a placeholder
    raise HTTPException(
        status_code=501,
        detail="Download functionality not yet implemented"
    )

# Background conversion processing
async def process_conversion(conversion_id: str, request: ConversionRequest):
    """Process document conversion in background"""
    
    status = active_conversions[conversion_id]
    
    try:
        status.status = 'processing'
        
        # Get converter class
        converter_class = CONVERTER_CLASSES[request.mode]
        converter = converter_class()
        
        # Process each file
        for i, file_path in enumerate(request.files):
            status.current_file = Path(file_path).name
            status.progress = i / len(request.files)
            
            try:
                # Determine output path based on option
                output_path = determine_output_path(
                    file_path, 
                    request.output_option, 
                    request.destination_path
                )
                
                # Convert file using universal converter
                result = converter.convert_document(file_path, output_path, request.mode)
                
                if result['success']:
                    status.results.append({
                        'source_file': file_path,
                        'output_file': result['html_path'],
                        'status': 'success',
                        'images_extracted': result.get('images_extracted', 0),
                        'images_dir': result.get('images_dir')
                    })
                    status.completed_files += 1
                else:
                    status.errors.append({
                        'source_file': file_path,
                        'error': result['message'],
                        'error_code': 'CONVERSION_FAILED'
                    })
                
            except Exception as e:
                status.errors.append({
                    'source_file': file_path,
                    'error': str(e),
                    'error_code': 'PROCESSING_ERROR'
                })
        
        # Mark completion
        status.progress = 1.0
        status.status = 'completed' if not status.errors else 'completed_with_errors'
        status.end_time = datetime.now().isoformat()
        
    except Exception as e:
        status.status = 'failed'
        status.errors.append({
            'error': str(e),
            'error_code': 'SYSTEM_ERROR',
            'traceback': traceback.format_exc()
        })
        status.end_time = datetime.now().isoformat()

def determine_output_path(file_path: str, output_option: str, destination_path: str = None) -> str:
    """Determine output file path based on conversion options"""
    
    source_path = Path(file_path)
    
    if output_option == 'beside':
        # Save HTML beside original file
        return str(source_path.with_suffix('.html'))
    
    elif output_option == 'mirrored':
        # Create mirrored directory structure
        # This is a simplified implementation - full version would handle directory mirroring
        dest_dir = Path(destination_path)
        dest_dir.mkdir(parents=True, exist_ok=True)
        return str(dest_dir / source_path.with_suffix('.html').name)
    
    elif output_option == 'single_folder':
        # Save all files to single folder
        dest_dir = Path(destination_path)
        dest_dir.mkdir(parents=True, exist_ok=True)
        return str(dest_dir / source_path.with_suffix('.html').name)
    
    else:
        raise ValueError(f"Unknown output option: {output_option}")

# Error handlers
@app.exception_handler(GiaconvertError)
async def giaconvert_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.error_code,
                "message": exc.message,
                "details": exc.details
            }
        }
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": f"HTTP_{exc.status_code}",
                "message": exc.detail
            }
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")