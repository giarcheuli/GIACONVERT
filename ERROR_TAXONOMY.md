# GIACONVERT Error Taxonomy & User-Friendly Messaging

## Overview
Comprehensive error classification and user-friendly message design for the GIACONVERT web application.

## Error Categories

### 1. File System Errors

#### 1.1 File Access Errors
```python
ERROR_TYPES = {
    'FILE_NOT_FOUND': {
        'code': 'FS001',
        'user_message': 'The file "{filename}" could not be found. It may have been moved or deleted.',
        'suggested_actions': [
            'Check if the file still exists in the original location',
            'Try selecting the file again',
            'Ensure you have permission to access the file'
        ]
    },
    'FILE_PERMISSION_DENIED': {
        'code': 'FS002', 
        'user_message': 'Permission denied accessing "{filename}". You may not have read access to this file.',
        'suggested_actions': [
            'Check file permissions',
            'Try running as administrator (if needed)',
            'Contact your system administrator'
        ]
    },
    'FILE_IN_USE': {
        'code': 'FS003',
        'user_message': 'The file "{filename}" is currently open in another application.',
        'suggested_actions': [
            'Close the file in Microsoft Word or other applications',
            'Try again after closing all applications using this file'
        ]
    }
}
```

#### 1.2 Directory Errors
```python
DIRECTORY_ERRORS = {
    'OUTPUT_DIR_NOT_WRITABLE': {
        'code': 'DIR001',
        'user_message': 'Cannot write to the output directory "{directory}". Check permissions.',
        'suggested_actions': [
            'Choose a different output directory',
            'Check directory permissions',
            'Ensure the directory exists'
        ]
    },
    'OUTPUT_DIR_FULL': {
        'code': 'DIR002',
        'user_message': 'Not enough disk space in "{directory}" to save converted files.',
        'suggested_actions': [
            'Free up disk space',
            'Choose a different output directory',
            'Delete unnecessary files'
        ]
    }
}
```

### 2. Document Processing Errors

#### 2.1 Document Format Errors
```python
DOCUMENT_ERRORS = {
    'INVALID_DOCX': {
        'code': 'DOC001',
        'user_message': 'The file "{filename}" is not a valid Word document or is corrupted.',
        'suggested_actions': [
            'Try opening the file in Microsoft Word to verify it works',
            'Save the document again from Word',
            'Use a different version of the document'
        ]
    },
    'UNSUPPORTED_DOCX_VERSION': {
        'code': 'DOC002',
        'user_message': 'The Word document "{filename}" uses features not yet supported.',
        'suggested_actions': [
            'Try using the Basic conversion mode instead',
            'Save the document in Word 2016+ format',
            'Report this issue for future support'
        ]
    },
    'PASSWORD_PROTECTED': {
        'code': 'DOC003',
        'user_message': 'The document "{filename}" is password protected and cannot be converted.',
        'suggested_actions': [
            'Remove password protection in Microsoft Word',
            'Save an unprotected copy of the document'
        ]
    }
}
```

#### 2.2 Content Processing Errors
```python
CONTENT_ERRORS = {
    'IMAGE_PROCESSING_FAILED': {
        'code': 'IMG001',
        'user_message': 'Some images in "{filename}" could not be processed. The document was converted but images may be missing.',
        'suggested_actions': [
            'Try using "Skip images" mode if images are not needed',
            'Check if images are in supported formats (JPEG, PNG, GIF)',
            'Try re-saving the document in Word'
        ]
    },
    'TABLE_CONVERSION_ERROR': {
        'code': 'TBL001',
        'user_message': 'Complex tables in "{filename}" may not display correctly in the HTML output.',
        'suggested_actions': [
            'Review the converted HTML file',
            'Simplify table structure in the original document if needed',
            'Use Basic conversion mode for simpler table handling'
        ]
    },
    'HEADER_FOOTER_ERROR': {
        'code': 'HF001',
        'user_message': 'Headers and footers in "{filename}" could not be fully converted.',
        'suggested_actions': [
            'Try using Enhanced mode instead of Complete mode',
            'Manually copy header/footer content if needed'
        ]
    }
}
```

### 3. System & Network Errors

#### 3.1 Memory & Performance
```python
SYSTEM_ERRORS = {
    'OUT_OF_MEMORY': {
        'code': 'SYS001',
        'user_message': 'The system ran out of memory while processing "{filename}". This usually happens with very large files.',
        'suggested_actions': [
            'Try converting smaller files or fewer files at once',
            'Close other applications to free up memory',
            'Try using Basic conversion mode'
        ]
    },
    'TIMEOUT': {
        'code': 'SYS002',
        'user_message': 'Converting "{filename}" is taking too long and was stopped.',
        'suggested_actions': [
            'Try converting this file individually',
            'Use Basic conversion mode for faster processing',
            'Check if the file is unusually large or complex'
        ]
    }
}
```

#### 3.2 Server Errors
```python
SERVER_ERRORS = {
    'SERVER_UNAVAILABLE': {
        'code': 'SRV001',
        'user_message': 'The conversion service is temporarily unavailable.',
        'suggested_actions': [
            'Wait a moment and try again',
            'Check if the GIACONVERT server is running',
            'Restart the application if problems persist'
        ]
    },
    'UPLOAD_FAILED': {
        'code': 'UPL001',
        'user_message': 'Failed to upload "{filename}". This may be due to file size or network issues.',
        'suggested_actions': [
            'Check your network connection',
            'Try uploading smaller files',
            'Refresh the page and try again'
        ]
    }
}
```

## Error Message Design Principles

### 1. User-Friendly Language
- **Avoid technical jargon**: Use "file" not "binary blob"
- **Be specific**: Include file names and paths when relevant
- **Be actionable**: Always suggest what the user can do next

### 2. Progressive Disclosure
```python
class ErrorMessage:
    def __init__(self, error_type, context):
        self.code = error_type['code']
        self.title = self.format_title(error_type, context)
        self.message = self.format_message(error_type, context)
        self.actions = error_type['suggested_actions']
        self.technical_details = None  # Hidden by default
    
    def format_message(self, error_type, context):
        return error_type['user_message'].format(**context)
```

### 3. Visual Design Guidelines
```css
/* Error Message Styling */
.error-message {
    border-left: 4px solid #dc3545;
    background-color: #f8d7da;
    color: #721c24;
    padding: 12px 16px;
    margin: 8px 0;
    border-radius: 4px;
}

.error-title {
    font-weight: bold;
    margin-bottom: 8px;
}

.error-actions {
    margin-top: 12px;
}

.error-action {
    display: block;
    margin: 4px 0;
    padding-left: 16px;
    position: relative;
}

.error-action::before {
    content: "→";
    position: absolute;
    left: 0;
    color: #6c757d;
}

.error-code {
    font-family: monospace;
    font-size: 0.8em;
    color: #6c757d;
    float: right;
}
```

## Error Context Collection

### Automatic Context Gathering
```python
def create_error_context(file_path, operation, error):
    """Collect context information for error reporting"""
    context = {
        'filename': Path(file_path).name,
        'filepath': str(file_path),
        'operation': operation,
        'timestamp': datetime.now().isoformat(),
        'file_size': get_file_size(file_path) if Path(file_path).exists() else 'unknown',
        'user_agent': request.headers.get('User-Agent', 'unknown'),
        'error_details': str(error)
    }
    return context
```

## Error Recovery Strategies

### 1. Automatic Retry
```python
RETRY_STRATEGIES = {
    'FILE_IN_USE': {
        'auto_retry': True,
        'retry_delay': 2,  # seconds
        'max_retries': 3
    },
    'TIMEOUT': {
        'auto_retry': False,  # Require user confirmation
        'retry_with_different_mode': True
    }
}
```

### 2. Graceful Degradation
```python
FALLBACK_MODES = {
    'IMAGE_PROCESSING_FAILED': 'skip_images',
    'HEADER_FOOTER_ERROR': 'enhanced_mode',
    'COMPLEX_TABLE_ERROR': 'basic_mode'
}
```

## Error Reporting & Analytics

### 1. User Feedback Collection
```javascript
// Optional error reporting
function showErrorFeedback(errorCode) {
    return `
        <div class="error-feedback">
            <p>Was this error message helpful?</p>
            <button onclick="reportError('${errorCode}', 'helpful')">Yes</button>
            <button onclick="reportError('${errorCode}', 'confusing')">No</button>
        </div>
    `;
}
```

### 2. Error Statistics
```python
# Track error frequency for improvement
error_stats = {
    'FS001': {'count': 15, 'last_seen': '2025-09-29'},
    'DOC001': {'count': 8, 'last_seen': '2025-09-28'},
    'IMG001': {'count': 23, 'last_seen': '2025-09-29'}
}
```

## Implementation in FastAPI

### Error Handler Example
```python
from fastapi import HTTPException
from fastapi.responses import JSONResponse

class GiaconvertError(Exception):
    def __init__(self, error_type, context):
        self.error_type = error_type
        self.context = context
        self.message = error_type['user_message'].format(**context)
        super().__init__(self.message)

@app.exception_handler(GiaconvertError)
async def giaconvert_error_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": exc.error_type['code'],
                "message": exc.message,
                "actions": exc.error_type['suggested_actions'],
                "context": exc.context
            }
        }
    )
```

## Testing Error Messages

### User Testing Checklist
- [ ] Messages are clear to non-technical users
- [ ] Suggested actions are actionable and helpful
- [ ] Error codes help with support requests
- [ ] Visual design draws attention without being alarming
- [ ] Recovery options are obvious and easy to use

### Automated Testing
```python
def test_error_message_formatting():
    """Test that error messages format correctly with various inputs"""
    error_type = ERROR_TYPES['FILE_NOT_FOUND']
    context = {'filename': 'test document.docx'}
    
    message = error_type['user_message'].format(**context)
    assert 'test document.docx' in message
    assert 'could not be found' in message
```

## Conclusion

This error taxonomy provides:
1. **Comprehensive Coverage**: All major error scenarios
2. **User-Friendly Messages**: Clear, actionable guidance
3. **Progressive Disclosure**: Simple messages with detailed help available
4. **Recovery Strategies**: Automatic and manual error recovery
5. **Continuous Improvement**: Feedback collection and analytics

The system should make errors feel less frustrating and more like helpful guidance for users.