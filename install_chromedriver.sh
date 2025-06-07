#!/bin/bash

# ChromeDriver Setup Script for macOS
echo "🔧 ChromeDriver Setup for macOS"
echo "==============================="
echo

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This script is for macOS only"
    exit 1
fi

# Check if Chrome is installed
if [ ! -d "/Applications/Google Chrome.app" ]; then
    echo "❌ Google Chrome is not installed"
    echo "📥 Please install Chrome first from: https://www.google.com/chrome/"
    exit 1
fi

echo "✅ Google Chrome found"

# Get Chrome version
CHROME_VERSION=$(/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version | cut -d' ' -f3 | cut -d'.' -f1)
echo "🔍 Chrome version: $CHROME_VERSION"

# Check if Homebrew is available
if command -v brew &> /dev/null; then
    echo "🍺 Homebrew found - using it to install ChromeDriver"
    
    # Install ChromeDriver via Homebrew
    brew install --cask chromedriver
    
    # Remove quarantine attribute (macOS security)
    echo "🔓 Removing quarantine attribute..."
    xattr -d com.apple.quarantine /opt/homebrew/bin/chromedriver 2>/dev/null || xattr -d com.apple.quarantine /usr/local/bin/chromedriver 2>/dev/null || true
    
    echo "✅ ChromeDriver installed via Homebrew"
    
else
    echo "🔄 Homebrew not found - manual installation"
    
    # Detect architecture
    ARCH=$(uname -m)
    if [[ "$ARCH" == "arm64" ]]; then
        PLATFORM="mac-arm64"
        echo "🖥️  Detected: Apple Silicon (ARM64)"
    else
        PLATFORM="mac-x64"
        echo "🖥️  Detected: Intel (x64)"
    fi
    
    # Create directory for ChromeDriver
    mkdir -p ~/bin
    
    # Download ChromeDriver
    echo "📥 Downloading ChromeDriver for $PLATFORM..."
    
    # Get the latest ChromeDriver version that matches Chrome
    DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
    if [ -z "$DRIVER_VERSION" ]; then
        echo "⚠️  Could not determine ChromeDriver version, using latest"
        DRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    fi
    
    echo "📦 ChromeDriver version: $DRIVER_VERSION"
    
    # Download and extract
    cd ~/bin
    curl -L -o chromedriver_$PLATFORM.zip "https://chromedriver.storage.googleapis.com/$DRIVER_VERSION/chromedriver_$PLATFORM.zip"
    
    if [ -f "chromedriver_$PLATFORM.zip" ]; then
        unzip -o chromedriver_$PLATFORM.zip
        rm chromedriver_$PLATFORM.zip
        chmod +x chromedriver
        
        # Remove quarantine attribute
        xattr -d com.apple.quarantine chromedriver 2>/dev/null || true
        
        echo "✅ ChromeDriver installed to ~/bin/chromedriver"
        
        # Add to PATH if not already there
        if [[ ":$PATH:" != *":$HOME/bin:"* ]]; then
            echo "🔧 Adding ~/bin to PATH"
            echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
            echo "📝 Added to ~/.zshrc - restart terminal or run: source ~/.zshrc"
        fi
    else
        echo "❌ Failed to download ChromeDriver"
        exit 1
    fi
fi

# Test ChromeDriver
echo "🧪 Testing ChromeDriver..."
if command -v chromedriver &> /dev/null; then
    INSTALLED_VERSION=$(chromedriver --version)
    echo "✅ ChromeDriver working: $INSTALLED_VERSION"
    echo ""
    echo "🎉 Setup complete! You can now run:"
    echo "   python send_single_selenium.py"
else
    echo "❌ ChromeDriver not found in PATH"
    echo "🔧 Try restarting your terminal or running: source ~/.zshrc"
fi
