# GIACONVERT Project Structure

```
GIACONVERT/
├── README.md                           # Comprehensive documentation
├── QUICK_START.md                      # This quick reference guide
├── IMAGE_SUPPORT_PLAN.md              # Image support implementation details
├── requirements.txt                    # Basic dependencies  
├── requirements_with_images.txt        # Enhanced dependencies (recommended)
├── setup.sh                           # Automated setup script (RUN ONCE)
├── giaconvert.py                      # Basic CLI application (text-only)
├── giaconvert_with_images.py          # Enhanced CLI with image support
├── giaconvert                         # Quick launcher script
├── create_test_document.py            # Basic test document generator
├── create_test_document_with_images.py # Enhanced test document generator
├── debug_images.py                    # Image debugging utility
└── test_documents/                    # Test files directory
    ├── sample_document.docx           # Basic sample Word document
    ├── sample_document.html           # Generated HTML file
    └── sample_document_with_images.docx # Sample with images
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

### Option 2: Enhanced Setup (With Images - Recommended)
1. **Install enhanced dependencies** (ONE-TIME ONLY):
   ```bash
   pip3 install -r requirements_with_images.txt
   ```

2. **Convert documents with image support** (use this every time):
   ```bash
   # External images (recommended for web):
   python3 giaconvert_with_images.py /path/to/your/documents --images external --optimize-images
   
   # Self-contained HTML files:
   python3 giaconvert_with_images.py /path/to/your/documents --images inline
   
   # Skip images (fastest):
   python3 giaconvert_with_images.py /path/to/your/documents --images skip
   
   # Show detailed progress:
   python3 giaconvert_with_images.py /path/to/your/documents --images external --verbose
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

### Enhanced Version (with Images)
- ✅ Everything from basic version PLUS:
- 🖼️ **Extracts and converts embedded images**
- 📁 **Multiple image handling modes** (external, inline, skip)
- 🔧 **Image optimization** (compression, resizing, format conversion)
- 📱 **Responsive image styling** (scales on different devices)
- 📊 **Enhanced progress reporting** (shows image count per document)

## Key Features

- **Smart**: Skips temporary files (~$ prefix)
- **Safe**: Never modifies original Word documents
- **Fast**: Efficient batch processing
- **Robust**: Comprehensive error handling
- **Clean**: Generates semantic HTML with inline CSS
- **Flexible**: Choose how to handle images based on your needs

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

### ⚡ Skip Images (`--images skip`)
- **Best for**: Text-only conversion, fastest processing
- **Output**: HTML with text and tables only
- **Pros**: Smallest files, fastest conversion
- **Example**: Perfect for text-heavy documents or quick conversion

GIACONVERT is ready to use! 🚀

## Quick Answers to Your Questions:

**Q: What does "one-time setup" mean?**  
A: You only run `./setup.sh` ONCE when you first install GIACONVERT. After that, you never need to run setup again. You can use `./giaconvert` as many times as you want!

**Q: How do I use GIACONVERT?**  
A: For basic conversion: `./giaconvert /path/to/your/folder`. For enhanced conversion with images: `python3 giaconvert_with_images.py /path/to/your/folder --images external`

**Q: What is verbose output?**  
A: When you add `--verbose`, GIACONVERT shows you more details about what it's doing (like which files it's processing, how many images were found, and more detailed error messages). Without `--verbose`, you only see the basic information.

**Q: Which image mode should I use?**  
A: Use `--images external --optimize-images` for web publishing (recommended), `--images inline` for self-contained files, or `--images skip` for fastest text-only conversion.

**Q: What's the difference between the basic and enhanced versions?**  
A: The basic version (`giaconvert.py`) handles text and tables only. The enhanced version (`giaconvert_with_images.py`) adds full image support with optimization options.