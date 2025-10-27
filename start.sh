#!/bin/bash
# Quick start script for Hindi Document Translator (macOS/Linux)

echo "========================================"
echo "Hindi Document Translator - Quick Start"
echo "========================================"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create virtual environment"
        exit 1
    fi
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate virtual environment"
    exit 1
fi

# Check if dependencies are installed
python -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
fi

# Check if font exists
if [ ! -f "fonts/NotoSansDevanagari-Regular.ttf" ]; then
    echo ""
    echo "WARNING: Hindi font not found!"
    echo "Please download NotoSansDevanagari-Regular.ttf and place it in the fonts/ directory"
    echo "Download from: https://fonts.google.com/noto/specimen/Noto+Sans+Devanagari"
    echo ""
    read -p "Press Enter to continue..."
fi

# Start the application
echo ""
echo "Starting Hindi Document Translator..."
echo ""
echo "The application will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
