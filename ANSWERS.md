# 🎉 GIACONVERT is Ready with Enhanced Capabilities!

## Your Questions Answered:

### 1. **What does "One-time setup" mean?**
**Answer:** You only need to run the setup ONCE when you first install GIACONVERT. After that, you can use the tool as many times as you want without running setup again!

```bash
# Basic setup (RUN THIS ONLY ONCE for text-only conversion):
./setup.sh

# Enhanced setup (RUN THIS ONLY ONCE for image support):
pip3 install -r requirements_with_images.txt

# THEN USE THESE EVERY TIME YOU WANT TO CONVERT DOCUMENTS:
./giaconvert ~/Documents/MyFolder                    # Basic version
python3 giaconvert_with_images.py ~/Documents --images external  # Enhanced version
```

### 2. **What are the different versions available?**
**Answer:** GIACONVERT now comes in two versions:

**Basic Version (`giaconvert.py` or `./giaconvert`):**
- ✅ Text formatting (bold, italic, colors, fonts)
- ✅ Tables with borders
- ✅ Paragraph alignment
- ❌ No image support
- ⚡ Faster, minimal dependencies

**Enhanced Version (`giaconvert_with_images.py`):**
- ✅ Everything from basic version
- ✅ Full image support (PNG, JPEG, GIF, BMP)
- ✅ Multiple image handling modes
- ✅ Image optimization and compression
- 🔧 More features, requires Pillow library

### 3. **How do I handle images in my documents?**
**Answer:** Use the enhanced version with image mode options:

```bash
# External images (best for web publishing)
python3 giaconvert_with_images.py ~/Documents --images external --optimize-images

# Self-contained HTML files (best for sharing)
python3 giaconvert_with_images.py ~/Documents --images inline

# Skip images (fastest conversion)
python3 giaconvert_with_images.py ~/Documents --images skip
```

### 4. **What is verbose output?**
**Answer:** Verbose means "show more details". Here's the difference:

**Normal output (without --verbose):**
- Shows basic progress
- Shows conversion summary
- Shows only essential information

**Verbose output (with --verbose):**
- Shows MORE detailed progress information
- Shows exactly which files are being processed
- Shows number of images processed per document
- Shows more detailed error messages if something goes wrong
- Shows additional debugging information

```bash
# Basic output (less details)
./giaconvert ~/Documents

# Verbose output (more details)
python3 giaconvert_with_images.py ~/Documents --images external --verbose
```

## How to Use GIACONVERT:

### Basic Version (Text and Tables Only):
```bash
# First Time (Setup - DO THIS ONCE):
cd /path/to/GIACONVERT
./setup.sh

# Every Time After That:
./giaconvert ~/Documents/MyWordDocs
./giaconvert ~/Documents/MyWordDocs --verbose  # Show more details
```

### Enhanced Version (With Image Support - Recommended):
```bash
# First Time (Setup - DO THIS ONCE):
cd /path/to/GIACONVERT
pip3 install -r requirements_with_images.txt

# Every Time After That:
# External images (recommended for web):
python3 giaconvert_with_images.py ~/Documents --images external --optimize-images

# Self-contained files:
python3 giaconvert_with_images.py ~/Documents --images inline

# Skip images (fastest):
python3 giaconvert_with_images.py ~/Documents --images skip

# Show detailed progress:
python3 giaconvert_with_images.py ~/Documents --images external --verbose
```

## What GIACONVERT Does:

### Basic Version:
1. 🔍 Finds all `.docx` files in your specified folder (and all subfolders)
2. 🔄 Converts each Word document to HTML format
3. 💾 Saves the HTML file in the same location as the original Word document
4. ✅ Keeps all your text formatting (bold, italic, colors, tables, etc.)

### Enhanced Version (Additional Features):
5. �️ **Extracts and converts embedded images**
6. 📁 **Saves images as separate files** (external mode) or **embeds them** (inline mode)
7. 🔧 **Optimizes images** for web use (optional compression and resizing)
8. 📊 **Shows image processing progress** (how many images per document)

**Your original Word documents are never changed or deleted - they stay exactly as they were!**

---

**GIACONVERT is now ready to use with advanced image support! Choose the version that best fits your needs!** 🚀

### Quick Decision Guide:
- **Need images?** → Use enhanced version with `--images external`
- **Text only?** → Use basic version with `./giaconvert`
- **Self-contained files?** → Use enhanced version with `--images inline`
- **Fastest conversion?** → Use enhanced version with `--images skip` or basic version