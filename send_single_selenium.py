#!/usr/bin/env python3
"""
Single message sender using Selenium
Perfect for testing the WhatsApp Web automation
"""

from whatsapp_selenium_bot import WhatsAppSeleniumBot
import time

def send_single():
    print("📱 Single WhatsApp Message Sender (Selenium)")
    print("=" * 45)
    print()
    
    contact = input("Enter contact name or phone number: ").strip()
    if not contact:
        print("❌ Contact is required")
        return
    
    message = input("Enter your message: ").strip()
    if not message:
        message = "Hello! This is a test message from the Selenium WhatsApp bot. 🤖"
    
    print(f"\n📋 Message Details:")
    print(f"👤 To: {contact}")
    print(f"💬 Message: {message}")
    print()
    
    confirm = input("Send this message? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Cancelled")
        return
    
    print("\n🚀 Initializing bot...")
    
    # Create bot instance
    bot = WhatsAppSeleniumBot(headless=False)
    
    try:
        # Setup and login
        if not bot.setup_driver():
            print("❌ Failed to setup browser")
            return
        
        if not bot.login_to_whatsapp():
            print("❌ Failed to login to WhatsApp")
            return
        
        # Find contact and send message
        if bot.find_contact(contact):
            if bot.send_message(message):
                print("✅ Message sent successfully!")
            else:
                print("❌ Failed to send message")
        else:
            print("❌ Could not find the contact")
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
    
    finally:
        # Keep browser open for a few seconds to see the result
        print("\n⏳ Keeping browser open for 5 seconds...")
        time.sleep(5)
        bot.close()

if __name__ == "__main__":
    send_single()
