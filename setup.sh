#!/bin/bash

# GIACONVERT Setup Script
# This script sets up the CLI app for converting Word documents to HTML

echo "🔧 Setting up GIACONVERT..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✅ Python 3 found"

# Install required packages
echo "📦 Installing required Python packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Packages installed successfully"
else
    echo "❌ Failed to install packages"
    exit 1
fi

# Make the script executable
chmod +x giaconvert.py

echo ""
echo "🎉 GIACONVERT setup completed successfully!"
echo ""
echo "Usage:"
echo "  python3 giaconvert.py /path/to/directory"
echo "  or"
echo "  ./giaconvert /path/to/directory"
echo ""
echo "Example:"
echo "  ./giaconvert ~/Documents/MyWordDocs"
echo ""
echo "The tool will convert all .docx files in the specified directory and its subdirectories to HTML format."