# 🎉 GIACONVERT is Ready!

## Your Questions Answered:

### 1. **What does "One-time setup" mean?**
**Answer:** You only need to run the setup ONCE when you first install GIACONVERT. After that, you can use the tool as many times as you want without running setup again!

```bash
# RUN THIS ONLY ONCE (when you first install):
./setup.sh

# THEN USE THIS EVERY TIME YOU WANT TO CONVERT DOCUMENTS:
./giaconvert ~/Documents/MyFolder
```

### 2. **Is "./giaconvert" the command to use the tool?**
**Answer:** Yes! I renamed it from `./convert.sh` to just `./giaconvert` - much easier to remember and type!

### 3. **Can we rename the python script?**
**Answer:** Done! I renamed `word_to_html.py` to `giaconvert.py`

### 4. **What is verbose output?**
**Answer:** Verbose means "show more details". Here's the difference:

**Normal output (without --verbose):**
- Shows basic progress
- Shows conversion summary
- Shows only essential information

**Verbose output (with --verbose):**
- Shows MORE detailed progress information
- Shows exactly which files are being processed
- Shows more detailed error messages if something goes wrong
- Shows additional debugging information

```bash
# Basic output (less details)
./giaconvert ~/Documents

# Verbose output (more details)
./giaconvert ~/Documents --verbose
```

## How to Use GIACONVERT:

### First Time (Setup - DO THIS ONCE):
```bash
cd /Users/giarcheulishvili/Documents/Tools/GIAutoConvert
./setup.sh
```

### Every Time After That:
```bash
# Convert all Word docs in a folder:
./giaconvert ~/Documents/MyWordDocs

# Show more details while converting:
./giaconvert ~/Documents/MyWordDocs --verbose

# You can also use the Python script directly:
python3 giaconvert.py ~/Documents/MyWordDocs
```

## What GIACONVERT Does:
1. 🔍 Finds all `.docx` files in your specified folder (and all subfolders)
2. 🔄 Converts each Word document to HTML format
3. 💾 Saves the HTML file in the same location as the original Word document
4. ✅ Keeps all your formatting (bold, italic, colors, tables, etc.)
5. 📊 Shows you a summary of what was converted

**Your original Word documents are never changed or deleted - they stay exactly as they were!**

---

**GIACONVERT is now ready to use! Just type `./giaconvert` followed by the path to your documents folder!** 🚀