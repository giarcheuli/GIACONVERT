# GIACONVERT - Advanced Word to HTML Converter CLI App

A powerful command-line tool that recursively searches through directories and converts Word documents (.docx) to HTML format while preserving formatting, structure, and images.

## Features

- 🔍 **Recursive Directory Search**: Automatically finds all Word documents in specified directory and subdirectories
- 📄 **Format Preservation**: Maintains text formatting (bold, italic, underline, colors, fonts)
- 📊 **Table Support**: Converts Word tables to HTML tables
- 🖼️ **Image Support**: Extracts and converts embedded images with multiple handling options
- 🎨 **Style Preservation**: Preserves text alignment and advanced styling
- 📝 **Progress Tracking**: Shows conversion progress and summary
- ⚡ **Fast Processing**: Efficiently processes multiple documents
- 🚫 **Smart Filtering**: Automatically skips temporary Word files (~$ files)
- 🔧 **Image Optimization**: Optional image compression and resizing for web

## Requirements

- macOS (or other Unix-like system)
- Python 3.6 or higher
- pip3

## Installation (One-time Setup)

**"One-time setup" means you only need to run this ONCE.** After the initial setup, you can use GIACONVERT anytime without running setup again!

### Option 1: Basic Installation (Text-only conversion)

1. **Clone or download this project to your Mac**

2. **Run the setup script** (ONLY NEEDED ONCE):
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

   This will:
   - Check for Python 3 installation
   - Install required Python packages (only needs to be done once)
   - Make the CLI tool executable

### Option 2: Full Installation (With Image Support - Recommended)

1. **Clone or download this project to your Mac**

2. **Install enhanced dependencies**:
   ```bash
   pip3 install -r requirements_with_images.txt
   ```

3. **Make scripts executable**:
   ```bash
   chmod +x giaconvert_with_images.py
   chmod +x giaconvert.py
   chmod +x giaconvert
   ```

## Usage

### Simple Usage (Text-only conversion)
```bash
./giaconvert /path/to/your/directory
```

### Enhanced Usage (With Image Support - Recommended)
```bash
# External images (separate files) - Best for web publishing
python3 giaconvert_with_images.py /path/to/your/directory --images external

# Inline images (embedded in HTML) - Best for self-contained files  
python3 giaconvert_with_images.py /path/to/your/directory --images inline

# Skip images (text-only) - Fastest conversion
python3 giaconvert_with_images.py /path/to/your/directory --images skip

# With image optimization (recommended for web)
python3 giaconvert_with_images.py /path/to/your/directory --images external --optimize-images
```

### Alternative Usage
```bash
python3 giaconvert.py /path/to/your/directory
```

### Examples

Convert all Word documents in your Documents folder (basic):
```bash
./giaconvert ~/Documents
```

Convert documents with image support (recommended):
```bash
python3 giaconvert_with_images.py ~/Documents --images external --optimize-images
```

Convert documents in a specific project folder:
```bash
python3 giaconvert_with_images.py ~/Projects/MyProject --images external
```

Create self-contained HTML files with embedded images:
```bash
python3 giaconvert_with_images.py ~/Documents --images inline
```

Show detailed output during conversion (**verbose** means "show more details"):
```bash
python3 giaconvert_with_images.py ~/Documents --images external --verbose
```

**What is verbose output?** When you use `--verbose`, GIACONVERT shows you:
- More detailed progress information
- Exactly which files are being processed
- Number of images processed per document
- More detailed error messages if something goes wrong
- Additional debugging information

Without `--verbose`, you only see the essential information. With `--verbose`, you see everything that's happening behind the scenes.

### Making it globally available (Optional)

To use the tool from anywhere on your Mac:

1. **Add to your PATH**:
   ```bash
   # Add this line to your ~/.zshrc file
   export PATH="$PATH:/Users/$(whoami)/Documents/Tools/GIAutoConvert"
   ```

2. **Reload your shell**:
   ```bash
   source ~/.zshrc
   ```

3. **Create a symlink** (alternative method):
   ```bash
   ln -s /Users/$(whoami)/Documents/Tools/GIAutoConvert/giaconvert /usr/local/bin/giaconvert
   ```

## Output

### Text-only Mode
- HTML files are created in the same location as the original Word documents
- Original Word files are preserved (not modified or deleted)
- File names are preserved with .html extension
- Example: `document.docx` → `document.html`

### With Image Support
- **External Images Mode**: Creates HTML file + `document_images/` folder containing image files
- **Inline Images Mode**: Creates single HTML file with images embedded as base64
- **Skip Images Mode**: Creates HTML file without images (same as text-only mode)

#### External Images Output Structure:
```
document.docx → document.html
                document_images/
                ├── image_001.jpg
                ├── image_002.png
                └── image_003.jpg
```

## Supported Features

### Text Formatting
- ✅ Bold text
- ✅ Italic text  
- ✅ Underlined text
- ✅ Font colors
- ✅ Font sizes
- ✅ Font families
- ✅ Text alignment (left, center, right, justify)

### Document Elements
- ✅ Paragraphs
- ✅ Tables with borders
- ✅ Line breaks
- ✅ **Images (PNG, JPEG, GIF, BMP)**
- ✅ **Image optimization and resizing**
- ✅ **Multiple image handling modes**
- ⚠️ Headers/Footers (not supported yet)

### Image Support Features
- ✅ **External Images**: Saves images as separate files with relative HTML paths
- ✅ **Inline Images**: Embeds images as base64 directly in HTML
- ✅ **Image Optimization**: Converts to JPEG and compresses for web use
- ✅ **Format Detection**: Automatically detects and preserves image formats
- ✅ **Responsive Styling**: Images scale properly on different screen sizes

## Error Handling

The tool includes comprehensive error handling:
- Skips corrupted or password-protected documents
- Reports conversion errors with details
- Shows summary of successful and failed conversions
- Continues processing other files even if some fail

## Troubleshooting

### Common Issues

1. **Permission Denied**:
   ```bash
   chmod +x giaconvert.py
   chmod +x setup.sh
   chmod +x giaconvert
   ```

2. **Module Not Found Error**:
   ```bash
   # For basic version
   pip3 install -r requirements.txt
   
   # For version with image support
   pip3 install -r requirements_with_images.txt
   ```

3. **Python Not Found**:
   - Install Python 3 from [python.org](https://www.python.org/downloads/)
   - Or use Homebrew: `brew install python3`

### Supported File Types

- ✅ `.docx` (Word 2007 and later)
- ❌ `.doc` (older Word format - not supported)
- ❌ `.rtf` (Rich Text Format - not supported)

## Technical Details

- Built with Python 3
- Uses `python-docx` for Word document parsing
- Uses `click` for command-line interface
- Uses `Pillow` for image processing and optimization
- Uses `lxml` for XML processing
- Generates clean, semantic HTML with inline CSS
- Preserves document structure, formatting, and images
- Supports multiple image handling strategies for different use cases

## Version Information

### Basic Version (`giaconvert.py`)
- Text and table conversion
- Fast processing
- Minimal dependencies

### Enhanced Version (`giaconvert_with_images.py`)
- Everything from basic version
- Full image support with multiple modes
- Image optimization capabilities
- Advanced error handling

## License

This tool is provided as-is for personal and educational use.

---

**Enjoy converting your Word documents to HTML! 🎉**