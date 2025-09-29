# GIACONVERT Image Support Implementation Plan

## Overview
Add comprehensive image support to GIACONVERT while maintaining the tool's simplicity and reliability.

## Technical Requirements

### Dependencies to Add
```txt
Pillow>=10.0.0  # Image processing and optimization
```

### New Command-Line Options
```bash
./giaconvert /path/to/docs --images inline    # Embed as base64
./giaconvert /path/to/docs --images external  # Save as separate files (default)
./giaconvert /path/to/docs --images skip      # Skip images entirely
./giaconvert /path/to/docs --optimize-images  # Compress images
```

## Implementation Strategy

### Phase 1: Basic Image Extraction
1. **Extract images from DOCX files**
   - Access document relationships
   - Extract image binary data
   - Determine image format (PNG, JPEG, etc.)

### Phase 2: Image Processing
1. **Image optimization** (optional)
   - Resize large images
   - Compress for web
   - Convert formats if needed

### Phase 3: HTML Integration
1. **External files approach**:
   - Save images to `{document_name}_images/` folder
   - Reference with relative paths in HTML
   
2. **Inline base64 approach**:
   - Convert images to base64
   - Embed directly in HTML

### Phase 4: Advanced Features
1. **Image metadata preservation**
   - Alt text from Word documents
   - Image dimensions and positioning
   - Captions and titles

## Code Architecture Changes

### New Methods Needed
```python
class WordToHTMLConverter:
    def extract_images_from_docx(self, doc, docx_path):
        """Extract all images from Word document"""
        
    def save_image_external(self, image_data, image_path, optimize=False):
        """Save image as external file with optional optimization"""
        
    def convert_image_to_base64(self, image_data, format):
        """Convert image to base64 string"""
        
    def process_inline_shapes(self, paragraph):
        """Process images within paragraphs"""
        
    def create_images_directory(self, html_path):
        """Create directory for external images"""
```

### File Structure Changes
```
document.docx → document.html
                document_images/
                ├── image_001.png
                ├── image_002.jpg
                └── image_003.png
```

## Image Handling Workflow

### 1. Document Analysis
- Scan for inline shapes (images)
- Extract image relationships
- Determine image formats and sizes

### 2. Image Processing
- Extract binary data
- Optionally optimize (resize/compress)
- Generate unique filenames

### 3. HTML Generation
- Replace image placeholders with HTML `<img>` tags
- Use appropriate src attribute (base64 or file path)
- Preserve image positioning and sizing

## Challenges & Solutions

### Challenge 1: Image Positioning
**Problem**: Word has complex image positioning
**Solution**: Convert to simpler CSS positioning (float, margin)

### Challenge 2: Large Images
**Problem**: Can make HTML files huge (base64) or slow to load
**Solution**: Optional image optimization and resizing

### Challenge 3: Image Formats
**Problem**: Word may contain various formats (WMF, EMF, PNG, JPEG)
**Solution**: Convert unsupported formats to PNG/JPEG

### Challenge 4: Broken Links
**Problem**: External images can be moved/deleted
**Solution**: Option to embed critical images, validate paths

## Implementation Priority

### High Priority
1. ✅ Basic image extraction from DOCX
2. ✅ External file saving with relative paths
3. ✅ HTML img tag generation

### Medium Priority
1. 🔄 Base64 inline embedding option
2. 🔄 Basic image optimization
3. 🔄 Command-line options for image handling

### Low Priority
1. ⚠️ Advanced positioning (text wrapping, etc.)
2. ⚠️ Image format conversion
3. ⚠️ Alt text and metadata preservation

## Testing Strategy

### Test Cases Needed
1. **Documents with various image types**
2. **Images in different positions** (inline, floating)
3. **Large images** (performance testing)
4. **Documents with many images** (batch processing)
5. **Corrupted or missing images** (error handling)

## Estimated Development Time
- **Phase 1** (Basic): 4-6 hours
- **Phase 2** (Processing): 2-3 hours  
- **Phase 3** (HTML Integration): 3-4 hours
- **Phase 4** (Advanced): 6-8 hours
- **Testing & Documentation**: 2-3 hours

**Total: ~17-24 hours of development**

## User Experience Impact

### Positive
- ✅ Complete document conversion
- ✅ Professional-looking HTML output
- ✅ Flexible image handling options

### Considerations
- 📁 More files generated (with external images)
- 💾 Larger HTML files (with inline images)
- ⏱️ Slightly longer conversion time

## Next Steps
1. Update requirements.txt with Pillow
2. Implement basic image extraction
3. Add command-line options
4. Create comprehensive tests
5. Update documentation