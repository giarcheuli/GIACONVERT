# GIACONVERT Project Structure

```
GIAutoConvert/
├── README.md                  # Comprehensive documentation
├── requirements.txt           # Python dependencies  
├── setup.sh                  # Automated setup script (RUN ONCE)
├── giaconvert.py             # Main CLI application
├── giaconvert                # Quick launcher script (MAIN COMMAND)
├── create_test_document.py   # Test document generator
└── test_documents/           # Test files directory
    ├── sample_document.docx  # Sample Word document
    └── sample_document.html  # Generated HTML file
```

## Quick Start

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

## What GIACONVERT does

- ✅ Recursively searches directories for .docx files
- ✅ Converts Word formatting to HTML/CSS
- ✅ Preserves text styles (bold, italic, underline, colors)
- ✅ Maintains paragraph alignment
- ✅ Converts tables with proper borders
- ✅ Creates HTML files in the same location as Word docs
- ✅ Shows progress and conversion summary
- ✅ Handles errors gracefully

## Key Features

- **Smart**: Skips temporary files (~$ prefix)
- **Safe**: Never modifies original Word documents
- **Fast**: Efficient batch processing
- **Robust**: Comprehensive error handling
- **Clean**: Generates semantic HTML with inline CSS

GIACONVERT is ready to use! 🚀

## Quick Answers to Your Questions:

**Q: What does "one-time setup" mean?**  
A: You only run `./setup.sh` ONCE when you first install GIACONVERT. After that, you never need to run setup again. You can use `./giaconvert` as many times as you want!

**Q: How do I use GIACONVERT?**  
A: Just type `./giaconvert /path/to/your/folder` - that's it!

**Q: What is verbose output?**  
A: When you add `--verbose`, GIACONVERT shows you more details about what it's doing (like which files it's processing and more detailed error messages). Without `--verbose`, you only see the basic information.