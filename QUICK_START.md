# GIACONVERT Quick Start Guide

## 🚀 Fastest Way to Get Started

### Web Application (Recommended)
1. **Double-click** `launch.py`
2. **Browser opens automatically** 
3. **Follow the wizard** to convert your documents

### Command Line (Advanced Users)
```bash
# One-time setup
./setup.sh

# Convert documents
python3 giaconvert_complete.py ~/Documents --images external --headers-footers include
```

## Project Structure

```
GIACONVERT/
├── 🌐 WEB APPLICATION
│   ├── launch.py                       # ← DOUBLE-CLICK THIS TO START!
│   ├── app.py                          # FastAPI backend server
│   └── web/                            # Frontend application
│       ├── index.html                  # Main web interface
│       ├── css/app.css                 # Custom styles
│       └── js/app.js                   # Vue.js application
├── 📖 DOCUMENTATION
│   ├── README.md                       # Comprehensive documentation
│   ├── QUICK_START.md                  # This quick reference guide
│   ├── WEB_APP_COMPLETE.md            # Web application documentation
│   ├── IMAGE_SUPPORT_PLAN.md          # Image support implementation details
│   ├── HEADERS_FOOTERS_PLAN.md        # Headers/footers implementation details
│   └── ANSWERS.md                      # FAQ and troubleshooting
├── 🖥️ COMMAND LINE TOOLS
│   ├── giaconvert.py                   # Basic CLI application (text-only)
│   ├── giaconvert_with_images.py       # Enhanced CLI with image support
│   ├── giaconvert_complete.py          # Complete CLI with all features
│   └── giaconvert                      # Quick launcher script
├── ⚙️ SETUP & CONFIGURATION
│   ├── setup.sh                        # Automated setup script
│   ├── requirements.txt                # Basic dependencies  
│   └── requirements_with_images.txt    # Enhanced dependencies
├── 🧪 TESTING & DEBUG
│   ├── test_converters.py              # Converter validation
│   ├── create_test_document.py         # Basic test document generator
│   ├── create_test_document_with_images.py # Image test document generator
│   ├── create_test_document_with_headers_footers.py # Headers/footers test generator
│   ├── debug_images.py                 # Image debugging utility
│   └── debug_headers_footers.py        # Headers/footers debugging utility
└── 📁 test_documents/                  # Test files directory
```

```
GIACONVERT/
├── README.md                           # Comprehensive documentation
├── QUICK_START.md                      # This quick reference guide
├── IMAGE_SUPPORT_PLAN.md              # Image support implementation details
├── HEADERS_FOOTERS_PLAN.md            # Headers/footers implementation details
├── requirements.txt                    # Basic dependencies  
├── requirements_with_images.txt        # Enhanced dependencies
├── setup.sh                           # Automated setup script (basic version)
├── giaconvert.py                      # Basic CLI application (text-only)
├── giaconvert_with_images.py          # Enhanced CLI with image support
├── giaconvert_complete.py             # Complete CLI with all features
├── giaconvert                         # Quick launcher script
├── create_test_document.py            # Basic test document generator
├── create_test_document_with_images.py # Image test document generator
├── create_test_document_with_headers_footers.py # Headers/footers test generator
├── debug_images.py                    # Image debugging utility
├── debug_headers_footers.py           # Headers/footers debugging utility
└── test_documents/                    # Test files directory
    ├── sample_document.docx           # Basic sample Word document
    ├── sample_document.html           # Generated HTML file
    ├── sample_document_with_images.docx # Sample with images
    └── sample_document_with_headers_footers.docx # Sample with headers/footers
```

## Quick Start

### Option 1: Basic Setup (Text-only)
1. **Setup** (ONE-TIME ONLY - you never need to do this again):
   ```bash
   ./setup.sh
   ```

2. **Convert documents** (use this every time):
   ```bash
   # EASIEST WAY - just type this:
   ./giaconvert /path/to/your/documents
   
   # Alternative ways:
   python3 giaconvert.py /path/to/your/documents
   
   # Show more details while converting:
   ./giaconvert /path/to/your/documents --verbose
   ```

### Option 3: Complete Setup (All Features - Recommended)
1. **Install complete dependencies** (ONE-TIME ONLY):
   ```bash
   pip3 install -r requirements_with_images.txt
   ```

2. **Convert documents with all features** (use this every time):
   ```bash
   # Complete conversion (recommended):
   python3 giaconvert_complete.py /path/to/your/documents --images external --headers-footers include --optimize-images
   
   # Print-optimized documents:
   python3 giaconvert_complete.py /path/to/your/documents --images inline --headers-footers print-only
   
   # Fast conversion (no images/headers):
   python3 giaconvert_complete.py /path/to/your/documents --images skip --headers-footers skip
   
   # Show detailed progress:
   python3 giaconvert_complete.py /path/to/your/documents --images external --headers-footers include --verbose
   ```

## What GIACONVERT does

### Basic Version
- ✅ Recursively searches directories for .docx files
- ✅ Converts Word formatting to HTML/CSS
- ✅ Preserves text styles (bold, italic, underline, colors)
- ✅ Maintains paragraph alignment
- ✅ Converts tables with proper borders
- ✅ Creates HTML files in the same location as Word docs
- ✅ Shows progress and conversion summary
- ✅ Handles errors gracefully

### Complete Version (with Images & Headers/Footers)
- ✅ Everything from enhanced version PLUS:
- � **Extracts and converts headers and footers**
- �️ **Professional print CSS** with proper page handling
- 📄 **Multiple headers/footers modes** (include, print-only, skip)
- 🏗️ **Semantic HTML structure** with proper elements
- 📱 **Responsive design** that works on all devices and printers

## Key Features

- **Smart**: Skips temporary files (~$ prefix)
- **Safe**: Never modifies original Word documents
- **Fast**: Efficient batch processing
- **Robust**: Comprehensive error handling
- **Clean**: Generates semantic HTML with inline CSS
- **Flexible**: Choose how to handle images and headers/footers based on your needs
- **Professional**: Print-ready CSS with proper page layout

## Image Handling Options

### 🔗 External Images (`--images external`)
- **Best for**: Web publishing, smaller HTML files
- **Output**: HTML + separate image files in `document_images/` folder
- **Pros**: Web-optimized, cacheable, smaller HTML files
- **Example**: Perfect for websites or when images will be used elsewhere

### 📎 Inline Images (`--images inline`)
- **Best for**: Self-contained files, email attachments
- **Output**: Single HTML file with embedded images
- **Pros**: Portable, no missing image files
- **Example**: Great for sharing complete documents via email

### ⚡ Skip Images & Headers/Footers (`--images skip --headers-footers skip`)
- **Best for**: Fastest processing, text-only conversion
- **Output**: HTML with text and tables only
- **Pros**: Smallest files, fastest conversion
- **Example**: Perfect for text-heavy documents or quick conversion

## Headers/Footers Handling Options

### 📄 Include Mode (`--headers-footers include`)
- **Best for**: Complete document representation
- **Output**: Headers/footers visible on screen and print
- **Pros**: Complete document conversion, professional appearance
- **Example**: Perfect for business documents, reports

### 🖨️ Print-Only Mode (`--headers-footers print-only`)
- **Best for**: Clean screen display with print headers/footers
- **Output**: Headers/footers only visible when printing
- **Pros**: Clean web view, professional print output
- **Example**: Perfect for web publishing with print capability

### 🚫 Skip Mode (`--headers-footers skip`)
- **Best for**: Clean document content without distractions
- **Output**: No headers/footers in output
- **Pros**: Fastest processing, clean content focus
- **Example**: Perfect for content extraction, clean web display

GIACONVERT is ready to use! 🚀

## Quick Answers to Your Questions:

**Q: What does "one-time setup" mean?**  
A: You only run `./setup.sh` ONCE when you first install GIACONVERT. After that, you never need to run setup again. You can use `./giaconvert` as many times as you want!

**Q: How do I use GIACONVERT?**  
A: For basic conversion: `./giaconvert /path/to/your/folder`. For enhanced conversion with images: `python3 giaconvert_with_images.py /path/to/your/folder --images external`

**Q: What is verbose output?**  
A: When you add `--verbose`, GIACONVERT shows you more details about what it's doing (like which files it's processing, how many images were found, and more detailed error messages). Without `--verbose`, you only see the basic information.

**Q: Which version should I use?**  
A: Use the **complete version** (`giaconvert_complete.py`) for full features including images and headers/footers. Use the enhanced version (`giaconvert_with_images.py`) if you only need images. Use the basic version (`giaconvert.py`) for simple text-only conversion.

**Q: Which image and headers/footers modes should I use?**  
A: For most cases: `--images external --headers-footers include --optimize-images`. For print documents: `--images inline --headers-footers print-only`. For fastest conversion: `--images skip --headers-footers skip`.

**Q: What's the difference between the three versions?**  
A: **Basic** handles text and tables. **Enhanced** adds images. **Complete** adds images, headers, footers, and professional print CSS.