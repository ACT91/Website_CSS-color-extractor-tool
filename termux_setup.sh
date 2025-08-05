#!/bin/bash
# Termux-specific setup script
echo "📱 CSS Color Extractor - Termux Setup"
echo "Made by ACT91 | https://github.com/ACT91"
echo "====================================="

# Update Termux packages
echo "Updating Termux packages..."
pkg update -y

# Install required packages
echo "Installing required packages..."
pkg install -y python python-pip git

# Install Python dependencies
echo "Installing Python dependencies..."
pip install requests beautifulsoup4 colorama

# Optional: Install Selenium (requires more setup)
read -p "Install Selenium for JS-heavy sites? (y/n): " install_selenium
if [[ $install_selenium == "y" || $install_selenium == "Y" ]]; then
    echo "Installing Selenium..."
    pkg install -y chromium
    pip install selenium
    echo "⚠️  Note: You may need to configure Chrome path manually"
fi

# Make scripts executable
chmod +x run.sh
chmod +x install.sh

echo ""
echo "Termux setup complete!"
echo "Run: ./run.sh"
echo "Or: python css-color-extractor.py"