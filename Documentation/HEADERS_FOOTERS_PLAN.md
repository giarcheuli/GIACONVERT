# GIACONVERT Headers and Footers Support Implementation Plan

## Overview
Add comprehensive headers and footers support to GIACONVERT while maintaining the tool's reliability and performance.

## Technical Analysis

### Word Document Structure
Word documents can have:
1. **Document Headers**: Content that appears at the top of every page
2. **Document Footers**: Content that appears at the bottom of every page
3. **Section Headers/Footers**: Different headers/footers for different sections
4. **First Page Different**: Special header/footer for the first page
5. **Even/Odd Different**: Different headers/footers for even and odd pages

### HTML Representation Challenges
HTML doesn't have native page concepts like Word, so we need to decide how to represent headers/footers:

#### Option 1: Page-Based Simulation
- Create CSS `@page` rules for print media
- Use `position: fixed` for screen display
- Simulate page breaks with CSS

#### Option 2: Document Structure Approach (Recommended)
- Add headers/footers as document sections
- Place at beginning and end of HTML document
- Use semantic HTML elements (`<header>`, `<footer>`)

#### Option 3: Repetitive Content
- Repeat headers/footers throughout document
- Insert at logical page break points

## Implementation Strategy

### Phase 1: Basic Header/Footer Detection
1. **Detect headers and footers** in Word documents
2. **Extract content** (text, formatting, images)
3. **Convert to HTML** with appropriate styling

### Phase 2: HTML Integration
1. **Document-level headers/footers** as semantic elements
2. **Print media CSS** for proper page rendering
3. **Screen display optimization**

### Phase 3: Advanced Features
1. **Page numbering** support
2. **Date/time fields** conversion
3. **Document properties** (author, title) in headers/footers

## Code Architecture Changes

### New Methods Needed
```python
class WordToHTMLConverter:
    def extract_headers_footers(self, doc):
        """Extract all headers and footers from document sections"""
        
    def convert_header_to_html(self, header):
        """Convert Word header to HTML header element"""
        
    def convert_footer_to_html(self, footer):
        """Convert Word footer to HTML footer element"""
        
    def process_header_footer_content(self, hf_element):
        """Process header/footer content including images and formatting"""
        
    def generate_print_css(self):
        """Generate CSS for proper print layout with headers/footers"""
```

### Word Document API
```python
# Access headers and footers
for section in doc.sections:
    header = section.header
    footer = section.footer
    first_page_header = section.first_page_header
    first_page_footer = section.first_page_footer
    even_page_header = section.even_page_header
    even_page_footer = section.even_page_footer
```

## HTML Output Structure

### Document Structure
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Print-specific styles */
        @media print {
            @page {
                margin-top: 2cm;
                margin-bottom: 2cm;
            }
            .document-header {
                position: running(header);
            }
            .document-footer {
                position: running(footer);
            }
        }
        
        /* Screen display styles */
        .document-header {
            position: sticky;
            top: 0;
            background: white;
            border-bottom: 1px solid #ccc;
            padding: 10px;
        }
        
        .document-footer {
            position: sticky;
            bottom: 0;
            background: white;
            border-top: 1px solid #ccc;
            padding: 10px;
        }
    </style>
</head>
<body>
    <header class="document-header">
        <!-- Header content -->
    </header>
    
    <main class="document-content">
        <!-- Document body content -->
    </main>
    
    <footer class="document-footer">
        <!-- Footer content -->
    </footer>
</body>
</html>
```

## Implementation Approach

### Command-Line Options
```bash
# Include headers and footers (default)
python3 giaconvert_with_images.py docs/ --headers-footers include

# Skip headers and footers
python3 giaconvert_with_images.py docs/ --headers-footers skip

# Headers and footers for print only
python3 giaconvert_with_images.py docs/ --headers-footers print-only
```

### Processing Workflow
1. **Document Analysis**
   - Scan all sections for headers/footers
   - Identify different header/footer types
   - Extract content and formatting

2. **Content Conversion**
   - Convert header/footer paragraphs to HTML
   - Process images in headers/footers
   - Handle special fields (page numbers, dates)

3. **HTML Generation**
   - Add semantic header/footer elements
   - Generate appropriate CSS
   - Ensure proper document structure

## Special Field Handling

### Page Numbers
- Convert `{PAGE}` field to CSS counter or JavaScript
- Handle different numbering formats

### Date/Time Fields
- Convert to static dates or dynamic JavaScript
- Preserve formatting

### Document Properties
- Convert author, title, subject fields
- Use document metadata where possible

## Challenges & Solutions

### Challenge 1: Page Context in HTML
**Problem**: HTML doesn't have pages like Word
**Solution**: Use CSS `@page` for print, sticky positioning for screen

### Challenge 2: Multiple Section Headers
**Problem**: Different sections may have different headers
**Solution**: Choose primary header or create section-based layout

### Challenge 3: Field Updates
**Problem**: Dynamic fields in Word (page numbers, dates)
**Solution**: Convert to static content or add JavaScript for dynamic updates

### Challenge 4: Complex Layouts
**Problem**: Headers/footers with tables, images, complex formatting
**Solution**: Use same conversion logic as document body

## Testing Strategy

### Test Cases Needed
1. **Simple text headers/footers**
2. **Headers/footers with images**
3. **Headers/footers with tables**
4. **Multiple section documents**
5. **First page different layouts**
6. **Page numbering and date fields**

## Estimated Development Time
- **Phase 1** (Detection & Extraction): 3-4 hours
- **Phase 2** (HTML Integration): 4-5 hours  
- **Phase 3** (Advanced Features): 4-6 hours
- **Testing & Documentation**: 2-3 hours

**Total: ~13-18 hours of development**

## User Experience Impact

### Positive
- ✅ Complete document conversion
- ✅ Professional document layout
- ✅ Print-friendly output
- ✅ Semantic HTML structure

### Considerations
- 📄 More complex HTML structure
- 🎨 May need CSS adjustments for some layouts
- 📱 Mobile display considerations

## Next Steps
1. Implement basic header/footer detection
2. Add HTML conversion logic
3. Create CSS for proper layout
4. Add command-line options
5. Test with various document types
6. Update documentation