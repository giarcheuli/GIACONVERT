# GIACONVERT - Word to HTML Converter CLI App

A command-line tool that recursively searches through directories and converts Word documents (.docx) to HTML format while preserving formatting and structure.

## Features

- 🔍 **Recursive Directory Search**: Automatically finds all Word documents in specified directory and subdirectories
- 📄 **Format Preservation**: Maintains text formatting (bold, italic, underline, colors, fonts)
- 📊 **Table Support**: Converts Word tables to HTML tables
- 🎨 **Style Preservation**: Preserves text alignment and basic styling
- 📝 **Progress Tracking**: Shows conversion progress and summary
- ⚡ **Fast Processing**: Efficiently processes multiple documents
- 🚫 **Smart Filtering**: Automatically skips temporary Word files (~$ files)

## Requirements

- macOS (or other Unix-like system)
- Python 3.6 or higher
- pip3

## Installation (One-time Setup)

**"One-time setup" means you only need to run this ONCE.** After the initial setup, you can use GIACONVERT anytime without running setup again!

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

## Usage

### Simple Usage (Recommended)
```bash
./giaconvert /path/to/your/directory
```

### Alternative Usage
```bash
python3 giaconvert.py /path/to/your/directory
```

### Examples

Convert all Word documents in your Documents folder:
```bash
./giaconvert ~/Documents
```

Convert documents in a specific project folder:
```bash
./giaconvert ~/Projects/MyProject
```

Show detailed output during conversion (**verbose** means "show more details"):
```bash
./giaconvert ~/Documents --verbose
```

**What is verbose output?** When you use `--verbose`, GIACONVERT shows you:
- More detailed progress information
- Exactly which files are being processed
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

- HTML files are created in the same location as the original Word documents
- Original Word files are preserved (not modified or deleted)
- File names are preserved with .html extension
- Example: `document.docx` → `document.html`

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
- ⚠️ Images (not supported yet)
- ⚠️ Headers/Footers (not supported yet)

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
   pip3 install -r requirements.txt
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
- Generates clean, semantic HTML with inline CSS
- Preserves document structure and formatting

## License

This tool is provided as-is for personal and educational use.

---

**Enjoy converting your Word documents to HTML! 🎉**