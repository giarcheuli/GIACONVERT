# GIACONVERT Storage Strategy Analysis

## Overview
Planning storage solutions for conversion history, user preferences, and application state.

## Storage Requirements

### Phase 1 (MVP) - No Persistent Storage
- **Session State**: Keep conversion progress in memory
- **User Preferences**: Store in browser localStorage
- **Error Logs**: Display in UI, no persistence required

### Phase 2 - Local Storage
- **Conversion History**: Track completed conversions
- **User Settings**: Persistent preferences across sessions
- **Error Logs**: Local file logging for debugging

### Phase 3 - Full Database (Future)
- **Multi-user Support**: Shared conversion history
- **Advanced Analytics**: Conversion statistics and insights

## Storage Technology Options

### 1. Browser localStorage (Phase 1)
```javascript
// Pros: Simple, no server-side setup, immediate availability
// Cons: Limited storage, browser-specific, no server access
localStorage.setItem('giaconvert_settings', JSON.stringify({
    defaultMode: 'enhanced',
    outputOption: 'beside_originals',
    lastUsedPaths: ['/Users/me/Documents']
}));
```

### 2. JSON Files (Phase 2)
```python
# Pros: Simple, human-readable, no database setup
# Cons: No concurrent access, manual file management
{
    "conversion_history": [
        {
            "timestamp": "2025-09-29T15:30:00Z",
            "source_files": ["doc1.docx", "doc2.docx"],
            "output_option": "mirrored",
            "mode": "complete",
            "success_count": 2,
            "error_count": 0
        }
    ],
    "user_preferences": {
        "default_mode": "enhanced",
        "last_input_dir": "/Users/me/Documents",
        "last_output_dir": "/Users/me/Converted"
    }
}
```

### 3. SQLite Database (Phase 2+)
```sql
-- Pros: ACID compliance, query capability, single file
-- Cons: More complex setup, binary format
CREATE TABLE conversions (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_path TEXT,
    output_path TEXT,
    mode TEXT,
    status TEXT,
    error_message TEXT
);

CREATE TABLE user_settings (
    key TEXT PRIMARY KEY,
    value TEXT
);
```

### 4. PostgreSQL/MySQL (Phase 3)
```sql
-- Pros: Full database features, multi-user, advanced queries
-- Cons: Complex setup, server requirement, overkill for local tool
-- Only for enterprise/cloud deployment
```

## Recommended Implementation Plan

### Phase 1 (Current): Browser-Only Storage
```javascript
// Store in browser localStorage
const settings = {
    defaultMode: 'enhanced',
    outputOption: 'beside_originals',
    recentPaths: []
};
localStorage.setItem('giaconvert_settings', JSON.stringify(settings));
```

### Phase 2: Local File Storage
```python
# config/user_data.py
import json
from pathlib import Path
from datetime import datetime

class UserDataManager:
    def __init__(self):
        self.data_dir = Path.home() / '.giaconvert'
        self.data_dir.mkdir(exist_ok=True)
        self.settings_file = self.data_dir / 'settings.json'
        self.history_file = self.data_dir / 'history.json'
    
    def save_conversion(self, source_files, output_option, mode, results):
        """Save conversion to history"""
        history = self.load_history()
        history.append({
            'timestamp': datetime.now().isoformat(),
            'source_files': [str(f) for f in source_files],
            'output_option': output_option,
            'mode': mode,
            'results': results
        })
        
        # Keep only last 100 conversions
        if len(history) > 100:
            history = history[-100:]
        
        self.history_file.write_text(json.dumps(history, indent=2))
    
    def load_settings(self):
        """Load user settings"""
        if self.settings_file.exists():
            return json.loads(self.settings_file.read_text())
        return self.default_settings()
    
    def save_settings(self, settings):
        """Save user settings"""
        self.settings_file.write_text(json.dumps(settings, indent=2))
```

## Data Schema Design

### Settings Schema
```json
{
    "default_mode": "enhanced|basic|complete",
    "default_output_option": "beside|mirrored|single_folder",
    "last_input_directory": "/path/to/last/input",
    "last_output_directory": "/path/to/last/output",
    "image_quality": 85,
    "max_image_width": 1200,
    "auto_open_results": true,
    "theme": "light|dark",
    "window_size": {"width": 1200, "height": 800}
}
```

### Conversion History Schema
```json
{
    "id": "uuid4",
    "timestamp": "2025-09-29T15:30:00Z",
    "input": {
        "files": ["/path/to/file1.docx", "/path/to/file2.docx"],
        "total_files": 2,
        "total_size_mb": 5.2
    },
    "settings": {
        "mode": "complete",
        "output_option": "mirrored",
        "destination": "/path/to/output"
    },
    "results": {
        "success_count": 2,
        "error_count": 0,
        "duration_seconds": 3.5,
        "output_files": ["/path/to/file1.html", "/path/to/file2.html"]
    },
    "errors": []
}
```

## Implementation Priority

1. **Phase 1**: Browser localStorage for basic settings
2. **Phase 2**: JSON files for conversion history
3. **Phase 2+**: Optional SQLite for advanced queries
4. **Phase 3**: Full database for multi-user features

## Security Considerations

- **Local Storage**: No sensitive data, user preferences only
- **File Paths**: Validate all paths to prevent directory traversal
- **History Cleanup**: Automatic cleanup of old conversion records
- **Error Logging**: Sanitize error messages to avoid exposing system info

## Performance Considerations

- **History Limit**: Keep max 100 recent conversions
- **Lazy Loading**: Load history only when needed
- **Background Cleanup**: Periodic cleanup of old temporary files
- **Index Creation**: SQLite indexes for timestamp and file path queries

## Testing Strategy

- **Unit Tests**: Test each storage method independently
- **Integration Tests**: Test FastAPI endpoints with storage
- **Migration Tests**: Test upgrades between storage versions
- **Performance Tests**: Test with large conversion histories

## Conclusion

**Recommended for GIACONVERT:**
- Start with browser localStorage (Phase 1)
- Add JSON file storage for history (Phase 2)
- Consider SQLite for advanced features (future)

This approach provides a clean upgrade path while keeping the initial implementation simple.