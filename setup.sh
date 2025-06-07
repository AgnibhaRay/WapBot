#!/bin/bash

# WhatsApp Bot Setup Script (Selenium Version)
echo "Setting up WhatsApp Bot with Selenium..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is required but not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "Setup complete! 🎉"
echo ""
echo "Available scripts:"
echo "1. Test with single message: python send_single_selenium.py"
echo "2. Demo with 3 messages: python selenium_demo.py" 
echo "3. Full bot (1000+ messages): python whatsapp_selenium_bot.py"
echo ""
echo "To run any script:"
echo "1. source .venv/bin/activate"
echo "2. python [script_name].py"
echo ""
echo "Features of Selenium version:"
echo "✅ More reliable than pywhatkit"
echo "✅ Real-time browser automation"
echo "✅ Better error handling"
echo "✅ No timing issues"
echo "✅ Works with contact names or phone numbers"
echo ""
echo "Make sure to:"
echo "- Have Chrome browser installed"
echo "- Keep your computer awake during message sending"
echo "- Use with caution and respect WhatsApp's terms of service"
