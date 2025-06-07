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
echo "🤖 WapBot by Agnibha Ray - Ultra-Fast WhatsApp Automation"
echo "========================================================="
echo ""
echo "Available scripts:"
echo "1. ⚡ Speed Test:           python speed_test.py"
echo "2. 🔥 Ultra-Fast Demo:      python ultra_fast_demo.py"
echo "3. 🔧 Single Message Test:  python send_single_selenium.py"
echo "4. 🎯 Demo (3 messages):    python selenium_demo.py" 
echo "5. 🚀 Full Bot (1000+):     python whatsapp_selenium_bot.py"
echo ""
echo "⚡ Speed Modes Available:"
echo "• Normal Mode:    30s delays (safe)"
echo "• Fast Mode:      3s delays (10x faster)"
echo "• Rapid Fire:     0.05s delays (200x faster!) ⚡"
echo "• Custom Mode:    Set your own speed"
echo ""
echo "To run any script:"
echo "1. source .venv/bin/activate"
echo "2. python [script_name].py"
echo ""
echo "🚀 Features of this Selenium version:"
echo "✅ ULTRA-FAST performance (up to 200x faster)"
echo "✅ Smart element caching for speed"
echo "✅ Optimized Chrome browser settings"
echo "✅ Multiple speed modes for different needs"
echo "✅ More reliable than pywhatkit"
echo "✅ Real-time browser automation"
echo "✅ Better error handling and recovery"
echo "✅ No timing issues"
echo "✅ Works with contact names or phone numbers"
echo ""
echo "⚠️ Important reminders:"
echo "- Have Chrome browser installed"
echo "- Keep your computer awake during message sending"
echo "- Use with caution and respect WhatsApp's terms of service"
echo "- Start with speed test or demo before full bot"
echo ""
echo "👨‍💻 Created by: Agnibha Ray"
echo "🔗 GitHub: @AgnibhaRay"
echo "🏆 Achievement: 200x performance optimization!"
