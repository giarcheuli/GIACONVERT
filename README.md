# GIACONVERT - Complete Word to HTML Converter

A powerful tool that converts Word documents (.docx) to HTML format while preserving formatting, structure, images, headers, and footers. Available as both a modern web application and command-line interface.

## 🌟 NEW: Web Application Interface

**GIACONVERT now includes a professional web application!** Perfect for business users who prefer a modern, intuitive interface.

### 🚀 Quick Start - Web App
1. **Double-click** `launch.py` to start the application
2. **Browser automatically opens** with the GIACONVERT interface
3. **Follow the wizard**: Select files → Choose settings → Convert
4. **Monitor progress** and view results

### ✨ Web App Features
- 🎨 **Modern Dashboard Interface** - Professional design for business users
- 📁 **File & Directory Selection** - Choose individual files or entire folders
- ⚙️ **Three Conversion Modes** - Basic, Enhanced (with images), Complete (with headers/footers)
- 📍 **Flexible Output Options** - Save beside originals, mirror directory structure, or single folder
- 📊 **Real-time Progress** - Live conversion tracking with individual file status
- 🔧 **Settings Persistence** - Remembers your preferences
- 🌐 **Cross-platform** - Works on all modern browsers
- 📱 **Responsive Design** - Works on desktop and mobile

## Features

- 🔍 **Recursive Directory Search**: Automatically finds all Word documents in specified directory and subdirectories
- 📄 **Format Preservation**: Maintains text formatting (bold, italic, underline, colors, fonts)
- 📊 **Table Support**: Converts Word tables to HTML tables
- 🖼️ **Image Support**: Extracts and converts embedded images with multiple handling options
- 📑 **Headers & Footers**: Preserves document headers and footers with flexible display options
- 🎨 **Style Preservation**: Preserves text alignment and advanced styling
- 📝 **Progress Tracking**: Shows conversion progress and summary
- ⚡ **Fast Processing**: Efficiently processes multiple documents
- 🚫 **Smart Filtering**: Automatically skips temporary Word files (~$ files)
- 🔧 **Image Optimization**: Optional image compression and resizing for web
- 🖨️ **Print Optimization**: Professional print CSS with proper page handling

## Requirements

- macOS (or other Unix-like system)
- Python 3.6 or higher
- pip3

## Installation & Setup

### Web Application (Recommended)
1. **Download or clone** this project
2. **Ensure Python 3.9+** is installed
3. **Run the setup** (one-time only):
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```
4. **Launch the application**:
   ```bash
   python3 launch.py
   # OR simply double-click launch.py
   ```

### Command-Line Interface (Advanced Users)

**"One-time setup" means you only need to run this ONCE.** After the initial setup, you can use GIACONVERT anytime without running setup again!

#### Option 1: Basic Installation (Text-only conversion)

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

#### Option 2: Complete Installation (With Images & Headers/Footers - Recommended)

1. **Clone or download this project to your Mac**

2. **Install complete dependencies**:
   ```bash
   pip3 install -r requirements_with_images.txt
   ```

3. **Make scripts executable**:
   ```bash
   chmod +x giaconvert_complete.py
   chmod +x giaconvert_with_images.py
   chmod +x giaconvert.py
   chmod +x giaconvert
   ```

## Usage

### Web Application (Recommended for Most Users)

Simply **double-click `launch.py`** and follow the intuitive web interface:

1. **Welcome Screen** - Overview and quick start
2. **File Selection** - Choose individual files or entire directories  
3. **Conversion Settings** - Select mode (Basic/Enhanced/Complete) and output options
4. **Progress Tracking** - Monitor real-time conversion progress
5. **Results** - View completed conversions and handle any errors

The web app automatically handles all the complex options and provides a professional user experience.

### Command-Line Interface (Advanced Users)

### CLI Simple Usage (Text-only conversion)
```bash
./giaconvert /path/to/your/directory
```

### CLI Enhanced Usage (With Images)
```bash
# External images (separate files) - Best for web publishing
python3 giaconvert_with_images.py /path/to/your/directory --images external

# Inline images (embedded in HTML) - Best for self-contained files  
python3 giaconvert_with_images.py /path/to/your/directory --images inline
```

### CLI Complete Usage (With Images & Headers/Footers)
```bash
# Complete conversion with all features (recommended)
python3 giaconvert_complete.py /path/to/your/directory --images external --headers-footers include --optimize-images

# Print-optimized documents
python3 giaconvert_complete.py /path/to/your/directory --images inline --headers-footers print-only

# Screen-only display (no headers/footers)
python3 giaconvert_complete.py /path/to/your/directory --images external --headers-footers skip

# Fast text-only conversion
python3 giaconvert_complete.py /path/to/your/directory --images skip --headers-footers skip
```

### CLI Alternative Usage
```bash
python3 giaconvert.py /path/to/your/directory
```

### CLI Examples

Convert all Word documents in your Documents folder (basic):
```bash
./giaconvert ~/Documents
```

Convert documents with complete feature set (recommended):
```bash
python3 giaconvert_complete.py ~/Documents --images external --headers-footers include --optimize-images
```

Convert documents for professional printing:
```bash
python3 giaconvert_complete.py ~/Projects/Reports --images inline --headers-footers print-only
```

Create self-contained HTML files with embedded images:
```bash
python3 giaconvert_complete.py ~/Documents --images inline --headers-footers include
```

Fast conversion without images or headers/footers:
```bash
python3 giaconvert_complete.py ~/Documents --images skip --headers-footers skip
```

Show detailed output during conversion (**verbose** means "show more details"):
```bash
python3 giaconvert_complete.py ~/Documents --images external --headers-footers include --verbose
```

**What is verbose output?** When you use `--verbose`, GIACONVERT shows you:
- More detailed progress information
- Exactly which files are being processed
- Number of images processed per document
- Headers and footers processing status
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

### With Complete Features (Images & Headers/Footers)
- **Complete Conversion**: Creates HTML file with all document elements
- **Headers/Footers Modes**:
  - **Include**: Shows headers/footers on screen and print
  - **Print-Only**: Headers/footers visible only when printing
  - **Skip**: Ignores headers/footers for clean screen display
- **Professional Layout**: Semantic HTML with proper print CSS

#### Complete Features Output Structure:
```
document.docx → document.html (with headers/footers)
                document_images/ (if external images)
                ├── image_001.jpg
                ├── image_002.png
                └── image_003.jpg
```

## Project Structure

```
GIACONVERT/
├── 🌐 Web Application
│   ├── launch.py              # Double-click to start (main launcher)
│   ├── app.py                 # FastAPI backend server
│   └── web/                   # Frontend files
│       ├── index.html         # Main application interface
│       ├── css/app.css        # Custom styles  
│       └── js/app.js          # Vue.js application logic
├── 🖥️ Command-Line Tools
│   ├── giaconvert.py          # Basic converter (text + tables)
│   ├── giaconvert_with_images.py  # Enhanced converter (+ images)
│   ├── giaconvert_complete.py     # Complete converter (+ headers/footers)
│   └── giaconvert             # CLI wrapper script
├── 📋 Setup & Configuration
│   ├── setup.sh               # One-time setup script
│   ├── requirements.txt       # Python dependencies
│   └── requirements_with_images.txt  # Extended dependencies
├── 📖 Documentation
│   ├── README.md              # This file
│   ├── QUICK_START.md         # Quick reference guide
│   ├── WEB_APP_COMPLETE.md    # Web app documentation
│   └── ANSWERS.md             # FAQ and troubleshooting
└── 🧪 Testing & Examples
    ├── test_documents/        # Sample Word documents
    ├── test_converters.py     # Converter validation
    └── create_test_document.py  # Test document generator
```

## Technical Architecture

### Web Application
- **Backend**: FastAPI (Python) with REST API endpoints
- **Frontend**: Vue.js 3 with Tailwind CSS for modern, responsive UI
- **File Handling**: Multi-file upload with directory structure preservation
- **Progress Tracking**: Real-time WebSocket-style polling for conversion status
- **Error Handling**: Comprehensive error taxonomy with user-friendly messages

### Conversion Engine
- **Core**: python-docx for Word document parsing
- **Images**: Pillow for image processing and optimization
- **Output**: Clean, semantic HTML with professional CSS
- **Modes**: Three conversion levels (Basic/Enhanced/Complete)

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
- ✅ **Headers and Footers**
- ✅ **Image optimization and resizing**
- ✅ **Multiple image handling modes**
- ✅ **Professional print CSS**

### Advanced Features
- ✅ **External Images**: Saves images as separate files with relative HTML paths
- ✅ **Inline Images**: Embeds images as base64 directly in HTML
- ✅ **Image Optimization**: Converts to JPEG and compresses for web use
- ✅ **Format Detection**: Automatically detects and preserves image formats
- ✅ **Responsive Styling**: Images scale properly on different screen sizes
- ✅ **Headers/Footers Support**: Three display modes (include, print-only, skip)
- ✅ **Semantic HTML**: Professional structure with proper elements
- ✅ **Print Optimization**: CSS @page rules for proper printing

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

### 🌐 Web Application (v1.0) - **Recommended**
- Modern dashboard interface with Vue.js + Tailwind CSS
- All conversion features accessible through intuitive wizard
- Real-time progress tracking and error handling
- Cross-platform browser compatibility
- Professional user experience for business users

### 🖥️ Command-Line Versions

#### Basic Version (`giaconvert.py`)
- Text and table conversion
- Fast processing
- Minimal dependencies

#### Enhanced Version (`giaconvert_with_images.py`)
- Everything from basic version
- Full image support with multiple modes
- Image optimization capabilities
- Advanced error handling

#### Complete Version (`giaconvert_complete.py`)
- Everything from enhanced version
- Headers and footers support
- Professional print CSS
- Semantic HTML structure
- Multiple headers/footers display modes

## License

This tool is provided as-is for personal and educational use.

---

**Enjoy converting your Word documents to HTML! 🎉**