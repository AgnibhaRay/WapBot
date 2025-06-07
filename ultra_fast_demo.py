#!/usr/bin/env python3
"""
Ultra-Fast WhatsApp Bot Demo - Maximum Speed Test
Sends 10 messages as fast as possible to demonstrate speed optimizations
"""

from whatsapp_selenium_bot import WhatsAppSeleniumBot
import time

def ultra_fast_demo():
    print("⚡ ULTRA-FAST WhatsApp Bot Demo")
    print("=" * 35)
    print("🔥 This will send 10 messages at MAXIMUM SPEED!")
    print("⚠️  WARNING: Very fast messaging - use responsibly!")
    print()
    
    contact = input("Enter contact name/number: ").strip()
    if not contact:
        print("❌ Contact required")
        return
    
    print(f"\n🎯 Target: {contact}")
    print("📱 Messages: 10")
    print("⚡ Speed: MAXIMUM (0.05s delays)")
    print("⏰ Estimated time: ~5 seconds")
    print()
    
    confirm = input("🚀 Launch ultra-fast demo? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Demo cancelled")
        return
    
    print("\n⚡ LAUNCHING ULTRA-FAST BOT...")
    print("🔥 Prepare for rapid fire messaging!")
    
    start_time = time.time()
    
    # Create bot in maximum speed mode
    bot = WhatsAppSeleniumBot(headless=False, fast_mode=True)
    
    try:
        # Use rapid fire method for maximum speed
        success = bot.send_rapid_fire_messages(contact, 10)
        
        end_time = time.time()
        total_time = end_time - start_time
        
        print(f"\n🏁 DEMO COMPLETED!")
        print(f"⏱️  Total time: {total_time:.2f} seconds")
        print(f"📊 Average: {10/total_time:.1f} messages per second")
        
        if success:
            print("✅ All messages sent successfully!")
            print("🔥 ULTRA-FAST mode is working perfectly!")
        else:
            print("⚠️  Some messages may have failed")
        
    except KeyboardInterrupt:
        print("\n⚠️ Demo stopped by user")
    except Exception as e:
        print(f"\n❌ Demo error: {str(e)}")
    finally:
        bot.close()
        print("\n🎉 Ultra-fast demo session completed!")

if __name__ == "__main__":
    try:
        ultra_fast_demo()
    except KeyboardInterrupt:
        print("\n👋 Demo cancelled!")
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
