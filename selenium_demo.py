#!/usr/bin/env python3
"""
Demo script for the Selenium WhatsApp bot
Sends 3 test messages with customizable delay
"""

from whatsapp_selenium_bot import WhatsAppSeleniumBot
import time

def demo():
    print("🤖 WhatsApp Selenium Bot Demo")
    print("=" * 30)
    print()
    print("This demo will send 3 test messages using Selenium.")
    print("✨ More reliable than the previous pywhatkit version!")
    print()
    
    contact = input("Enter contact name or phone number (e.g., 'John Doe' or '+1234567890'): ").strip()
    
    if not contact:
        print("❌ Contact name/number is required")
        return
    
    try:
        delay = int(input("Enter delay between messages in seconds (default 10): ") or "10")
        if delay < 1:
            delay = 10
    except ValueError:
        delay = 10
    
    print(f"\n📋 Demo Configuration:")
    print(f"👤 Contact: {contact}")
    print(f"📱 Messages: 3")
    print(f"⏱️ Delay: {delay} seconds")
    print()
    print("📝 The bot will:")
    print("1. Open Chrome browser")
    print("2. Navigate to WhatsApp Web")
    print("3. Wait for you to scan QR code")
    print("4. Find your contact")
    print("5. Send 3 test messages")
    print()
    
    confirm = input("Continue with demo? (y/n): ").lower().strip()
    
    if confirm != 'y':
        print("❌ Demo cancelled")
        return
    
    print("\n🚀 Starting demo...")
    
    # Create and run the bot
    bot = WhatsAppSeleniumBot(headless=False)
    success = bot.send_multiple_messages(contact, 3, delay)
    
    if success:
        print("\n🎉 Demo completed successfully!")
    else:
        print("\n❌ Demo encountered some issues.")
    
    print("\nIf the demo worked well, you can run the full bot with:")
    print("python whatsapp_selenium_bot.py")

if __name__ == "__main__":
    demo()
