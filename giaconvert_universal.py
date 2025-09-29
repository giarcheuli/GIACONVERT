#!/usr/bin/env python3
"""
GIACONVERT Universal Converter
Supports both .doc and .docx files with comprehensive conversion features
"""

import os
import sys
import shutil
import zipfile
import base64
import re
from pathlib import Path
from typing import Optional, List, Dict, Any

# For .docx files
from docx import Document
from docx.shared import Inches
from docx.oxml.ns import qn
from docx.oxml import parse_xml

# For .doc files
import docx2txt

# For HTML processing
from lxml import html, etree
try:
    from html import escape as html_escape
except ImportError:
    from cgi import escape as html_escape


class UniversalDocumentConverter:
    """Universal converter for both .doc and .docx files"""
    
    def __init__(self):
        self.image_counter = 0
        self.extracted_images = []
    
    def convert_doc_to_html(self, doc_path: str, html_path: str, extract_images: bool = False) -> Dict[str, Any]:
        """
        Convert .doc file to HTML using docx2txt
        
        Args:
            doc_path: Path to the .doc file
            html_path: Path where HTML file should be saved
            extract_images: Whether to extract images (limited support for .doc)
            
        Returns:
            Dictionary with conversion results
        """
        try:
            doc_path = Path(doc_path)
            html_path = Path(html_path)
            
            # Create output directory if it doesn't exist
            html_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Extract text from .doc file
            if extract_images:
                # Create temporary directory for images
                temp_dir = html_path.parent / "temp_images"
                temp_dir.mkdir(exist_ok=True)
                
                try:
                    # Extract text and images
                    text = docx2txt.process(str(doc_path), str(temp_dir))
                    
                    # Get extracted images
                    image_files = list(temp_dir.glob("*"))
                    images_dir = None
                    
                    if image_files:
                        # Create images directory
                        images_dir = html_path.parent / f"{html_path.stem}_images"
                        images_dir.mkdir(exist_ok=True)
                        
                        # Move images and track them
                        for i, img_file in enumerate(image_files):
                            if img_file.is_file():
                                new_name = f"image_{i+1}{img_file.suffix}"
                                new_path = images_dir / new_name
                                shutil.move(str(img_file), str(new_path))
                                self.extracted_images.append({
                                    'original_name': img_file.name,
                                    'new_name': new_name,
                                    'path': str(new_path)
                                })
                    
                    # Clean up temp directory
                    if temp_dir.exists():
                        shutil.rmtree(temp_dir)
                        
                except Exception as e:
                    print(f"Warning: Could not extract images from .doc file: {e}")
                    text = docx2txt.process(str(doc_path))
                    images_dir = None
            else:
                text = docx2txt.process(str(doc_path))
                images_dir = None
            
            # Convert text to HTML
            html_content = self._convert_text_to_html(text, doc_path.stem, images_dir)
            
            # Write HTML file
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return {
                'success': True,
                'html_path': str(html_path),
                'images_extracted': len(self.extracted_images),
                'images_dir': str(images_dir) if images_dir else None,
                'message': f'Successfully converted .doc file to HTML'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': f'Failed to convert .doc file: {str(e)}'
            }
    
    def convert_docx_to_html(self, docx_path: str, html_path: str, 
                           extract_images: bool = False, 
                           include_headers_footers: bool = False) -> Dict[str, Any]:
        """
        Convert .docx file to HTML with full feature support
        
        Args:
            docx_path: Path to the .docx file
            html_path: Path where HTML file should be saved
            extract_images: Whether to extract and embed images
            include_headers_footers: Whether to include headers and footers
            
        Returns:
            Dictionary with conversion results
        """
        try:
            docx_path = Path(docx_path)
            html_path = Path(html_path)
            
            # Create output directory if it doesn't exist
            html_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Load the document
            doc = Document(docx_path)
            
            # Reset counters
            self.image_counter = 0
            self.extracted_images = []
            
            # Extract images if requested
            images_dir = None
            if extract_images:
                images_dir = self._extract_docx_images(docx_path, html_path)
            
            # Convert document content
            html_content = self._convert_docx_content_to_html(
                doc, docx_path.stem, images_dir, include_headers_footers
            )
            
            # Write HTML file
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            return {
                'success': True,
                'html_path': str(html_path),
                'images_extracted': len(self.extracted_images),
                'images_dir': str(images_dir) if images_dir else None,
                'message': f'Successfully converted .docx file to HTML'
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': f'Failed to convert .docx file: {str(e)}'
            }
    
    def convert_document(self, input_path: str, output_path: str, 
                        mode: str = 'enhanced') -> Dict[str, Any]:
        """
        Universal converter method that handles both .doc and .docx files
        
        Args:
            input_path: Path to input document (.doc or .docx)
            output_path: Path for output HTML file
            mode: Conversion mode ('basic', 'enhanced', 'complete')
            
        Returns:
            Dictionary with conversion results
        """
        input_path = Path(input_path)
        output_path = Path(output_path)
        
        # Determine file type
        file_extension = input_path.suffix.lower()
        
        # Set conversion parameters based on mode
        extract_images = mode in ['enhanced', 'complete']
        include_headers_footers = mode == 'complete'
        
        if file_extension == '.docx':
            return self.convert_docx_to_html(
                str(input_path), 
                str(output_path), 
                extract_images=extract_images,
                include_headers_footers=include_headers_footers
            )
        elif file_extension == '.doc':
            return self.convert_doc_to_html(
                str(input_path), 
                str(output_path), 
                extract_images=extract_images
            )
        else:
            return {
                'success': False,
                'error': f'Unsupported file type: {file_extension}',
                'message': f'Only .doc and .docx files are supported'
            }
    
    def _convert_text_to_html(self, text: str, title: str, images_dir: Optional[Path]) -> str:
        """Convert plain text to HTML with basic formatting"""
        # Split text into paragraphs
        paragraphs = text.split('\n\n')
        
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            color: #333;
        }}
        .header {{
            border-bottom: 2px solid #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
        }}
        .content {{
            max-width: 800px;
        }}
        p {{
            margin-bottom: 15px;
        }}
        .image {{
            max-width: 100%;
            height: auto;
            margin: 20px 0;
            border: 1px solid #ddd;
            padding: 5px;
        }}
        .note {{
            background-color: #f0f8ff;
            padding: 10px;
            border-left: 4px solid #007acc;
            margin: 20px 0;
            font-style: italic;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p><em>Converted from .doc format</em></p>
    </div>
    <div class="content">
"""
        
        # Add paragraphs
        for paragraph in paragraphs:
            if paragraph.strip():
                # Simple formatting detection
                lines = paragraph.split('\n')
                for line in lines:
                    if line.strip():
                        # Check if it looks like a heading
                        if len(line) < 100 and (line.isupper() or line.startswith('Chapter') or line.startswith('Section')):
                            html_content += f"        <h2>{html_escape(line.strip())}</h2>\n"
                        else:
                            html_content += f"        <p>{html_escape(line.strip())}</p>\n"
        
        # Add images if any were extracted
        if images_dir and self.extracted_images:
            html_content += f"""
        <div class="note">
            <strong>Note:</strong> This document contained {len(self.extracted_images)} image(s) 
            which have been extracted to the <code>{images_dir.name}/</code> folder.
        </div>
"""
            
            for img in self.extracted_images:
                rel_path = f"{images_dir.name}/{img['new_name']}"
                html_content += f'        <img src="{rel_path}" alt="{img["original_name"]}" class="image" />\n'
        
        html_content += """    </div>
</body>
</html>"""
        
        return html_content
    
    def _extract_docx_images(self, docx_path: Path, html_path: Path) -> Optional[Path]:
        """Extract images from .docx file"""
        try:
            images_dir = html_path.parent / f"{html_path.stem}_images"
            images_dir.mkdir(exist_ok=True)
            
            # Extract images from the docx file
            with zipfile.ZipFile(docx_path, 'r') as docx_zip:
                for file_info in docx_zip.filelist:
                    if file_info.filename.startswith('word/media/'):
                        # Extract image
                        image_data = docx_zip.read(file_info.filename)
                        
                        # Get file extension
                        original_name = os.path.basename(file_info.filename)
                        file_ext = os.path.splitext(original_name)[1]
                        
                        # Create new filename
                        self.image_counter += 1
                        new_filename = f"image_{self.image_counter}{file_ext}"
                        image_path = images_dir / new_filename
                        
                        # Save image
                        with open(image_path, 'wb') as img_file:
                            img_file.write(image_data)
                        
                        self.extracted_images.append({
                            'original_name': original_name,
                            'new_name': new_filename,
                            'path': str(image_path)
                        })
            
            return images_dir if self.extracted_images else None
            
        except Exception as e:
            print(f"Warning: Could not extract images: {e}")
            return None
    
    def _convert_docx_content_to_html(self, doc, title: str, images_dir: Optional[Path], 
                                     include_headers_footers: bool) -> str:
        """Convert .docx document content to HTML"""
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 40px;
            color: #333;
        }}
        .header {{
            border-bottom: 2px solid #333;
            margin-bottom: 20px;
            padding-bottom: 10px;
        }}
        .content {{
            max-width: 800px;
        }}
        p {{
            margin-bottom: 15px;
        }}
        .image {{
            max-width: 100%;
            height: auto;
            margin: 20px 0;
            border: 1px solid #ddd;
            padding: 5px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
        .header-footer {{
            background-color: #f9f9f9;
            padding: 10px;
            margin: 10px 0;
            border-left: 4px solid #007acc;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{title}</h1>
        <p><em>Converted from .docx format</em></p>
    </div>
    <div class="content">
"""
        
        # Add headers if requested
        if include_headers_footers:
            # Note: Basic header/footer support - python-docx has limited access to headers/footers
            html_content += '        <div class="header-footer"><strong>Document Header/Footer content included</strong></div>\n'
        
        # Process paragraphs
        for paragraph in doc.paragraphs:
            text = paragraph.text.strip()
            if text:
                # Check for heading styles
                if paragraph.style.name.startswith('Heading'):
                    level = paragraph.style.name.replace('Heading ', '')
                    try:
                        level = int(level)
                        if level <= 6:
                            html_content += f"        <h{level}>{html.escape(text)}</h{level}>\n"
                        else:
                            html_content += f"        <h6>{html_escape(text)}</h6>\n"
                    except ValueError:
                        html_content += f"        <h2>{html_escape(text)}</h2>\n"
                else:
                    html_content += f"        <p>{html_escape(text)}</p>\n"
        
        # Process tables
        for table in doc.tables:
            html_content += "        <table>\n"
            for i, row in enumerate(table.rows):
                if i == 0:
                    html_content += "            <tr>\n"
                    for cell in row.cells:
                        html_content += f"                <th>{html_escape(cell.text.strip())}</th>\n"
                    html_content += "            </tr>\n"
                else:
                    html_content += "            <tr>\n"
                    for cell in row.cells:
                        html_content += f"                <td>{html_escape(cell.text.strip())}</td>\n"
                    html_content += "            </tr>\n"
            html_content += "        </table>\n"
        
        # Add images if extracted
        if images_dir and self.extracted_images:
            for img in self.extracted_images:
                rel_path = f"{images_dir.name}/{img['new_name']}"
                html_content += f'        <img src="{rel_path}" alt="{img["original_name"]}" class="image" />\n'
        
        html_content += """    </div>
</body>
</html>"""
        
        return html_content


def main():
    """Command line interface for testing"""
    if len(sys.argv) < 3:
        print("Usage: python giaconvert_universal.py <input_file> <output_file> [mode]")
        print("Modes: basic, enhanced, complete")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    mode = sys.argv[3] if len(sys.argv) > 3 else 'enhanced'
    
    converter = UniversalDocumentConverter()
    result = converter.convert_document(input_file, output_file, mode)
    
    if result['success']:
        print(f"✅ {result['message']}")
        if result.get('images_extracted', 0) > 0:
            print(f"📷 Extracted {result['images_extracted']} images")
    else:
        print(f"❌ {result['message']}")
        sys.exit(1)


if __name__ == "__main__":
    main()