#!/bin/bash
echo "🎨 CSS Color Extractor - Installation Script"
echo "Made by ACT91 | https://github.com/ACT91"
echo "=========================================="

# Detect platform
if [[ "$PREFIX" == *"com.termux"* ]]; then
    echo "📱 Detected: Termux (Android)"
    PKG_MANAGER="pkg"
    PYTHON_CMD="python"
elif command -v apt &> /dev/null; then
    echo "🐧 Detected: Debian/Ubuntu Linux"
    PKG_MANAGER="apt"
    PYTHON_CMD="python3"
elif command -v yum &> /dev/null; then
    echo "🐧 Detected: RedHat/CentOS Linux"
    PKG_MANAGER="yum"
    PYTHON_CMD="python3"
elif command -v pacman &> /dev/null; then
    echo "🐧 Detected: Arch Linux"
    PKG_MANAGER="pacman"
    PYTHON_CMD="python3"
else
    echo "🐧 Detected: Generic Linux"
    PKG_MANAGER="unknown"
    PYTHON_CMD="python3"
fi

echo ""
echo "Installing dependencies..."

# Install Python if not available
if ! command -v $PYTHON_CMD &> /dev/null && ! command -v python &> /dev/null; then
    echo "Installing Python..."
    if [[ "$PKG_MANAGER" == "pkg" ]]; then
        pkg update && pkg install python
    elif [[ "$PKG_MANAGER" == "apt" ]]; then
        sudo apt update && sudo apt install python3 python3-pip
    elif [[ "$PKG_MANAGER" == "yum" ]]; then
        sudo yum install python3 python3-pip
    elif [[ "$PKG_MANAGER" == "pacman" ]]; then
        sudo pacman -S python python-pip
    fi
fi

# Install pip packages
echo "Installing Python packages..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt
elif command -v pip &> /dev/null; then
    pip install -r requirements.txt
else
    echo "❌ pip not found. Please install pip manually."
    exit 1
fi

# Make scripts executable
chmod +x run.sh

echo ""
echo "Installation complete!"
echo "Run the tool with: ./run.sh"
echo "Or use: $PYTHON_CMD css-color-extractor.py"