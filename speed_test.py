#!/usr/bin/env python3
"""
WhatsApp Bot Speed Test - Demonstrates optimized performance
This script tests the bot's speed capabilities with different modes
"""

from whatsapp_selenium_bot import WhatsAppSeleniumBot
import time

def speed_demo():
    print("⚡ WhatsApp Bot Speed Test Demo")
    print("=" * 40)
    print()
    
    contact = input("Enter contact name/number for speed test: ").strip()
    if not contact:
        print("❌ Contact required for speed test")
        return
    
    print("\n🚀 Testing different speed modes...")
    print("This will send 5 messages in each mode for comparison")
    print()
    
    confirm = input("Continue with speed test? (y/n): ").lower().strip()
    if confirm != 'y':
        print("❌ Speed test cancelled")
        return
    
    # Test 1: Normal Mode
    print("\n📊 TEST 1: Normal Mode (3s delays)")
    print("-" * 30)
    start_time = time.time()
    
    bot1 = WhatsAppSeleniumBot(headless=False, fast_mode=False)
    try:
        bot1.send_multiple_messages(contact, 5, 3)
    except:
        pass
    finally:
        bot1.close()
    
    normal_time = time.time() - start_time
    print(f"⏱️ Normal mode completed in: {normal_time:.1f} seconds")
    
    time.sleep(2)  # Brief pause between tests
    
    # Test 2: Fast Mode
    print("\n📊 TEST 2: Fast Mode (0.5s delays)")
    print("-" * 30)
    start_time = time.time()
    
    bot2 = WhatsAppSeleniumBot(headless=False, fast_mode=True)
    try:
        bot2.send_multiple_messages(contact, 5, 0.5)
    except:
        pass
    finally:
        bot2.close()
    
    fast_time = time.time() - start_time
    print(f"⏱️ Fast mode completed in: {fast_time:.1f} seconds")
    
    time.sleep(2)  # Brief pause between tests
    
    # Test 3: Rapid Fire Mode
    print("\n📊 TEST 3: Rapid Fire Mode (0.05s delays)")
    print("-" * 30)
    start_time = time.time()
    
    bot3 = WhatsAppSeleniumBot(headless=False, fast_mode=True)
    try:
        bot3.send_rapid_fire_messages(contact, 5)
    except:
        pass
    finally:
        bot3.close()
    
    rapid_time = time.time() - start_time
    print(f"⏱️ Rapid fire mode completed in: {rapid_time:.1f} seconds")
    
    # Results summary
    print("\n🏆 SPEED TEST RESULTS")
    print("=" * 30)
    print(f"📊 Normal Mode:    {normal_time:.1f}s")
    print(f"🚀 Fast Mode:      {fast_time:.1f}s")
    print(f"⚡ Rapid Fire:     {rapid_time:.1f}s")
    print()
    
    if fast_time < normal_time:
        speedup_fast = normal_time / fast_time
        print(f"📈 Fast Mode is {speedup_fast:.1f}x faster than Normal")
    
    if rapid_time < fast_time:
        speedup_rapid = fast_time / rapid_time
        print(f"⚡ Rapid Fire is {speedup_rapid:.1f}x faster than Fast Mode")
    
    if rapid_time < normal_time:
        speedup_total = normal_time / rapid_time
        print(f"🔥 Rapid Fire is {speedup_total:.1f}x faster than Normal Mode!")
    
    print("\n💡 For 1000 messages:")
    print(f"📊 Normal Mode would take:    ~{(normal_time * 200):.0f} seconds ({(normal_time * 200)/60:.1f} minutes)")
    print(f"🚀 Fast Mode would take:      ~{(fast_time * 200):.0f} seconds ({(fast_time * 200)/60:.1f} minutes)")
    print(f"⚡ Rapid Fire would take:     ~{(rapid_time * 200):.0f} seconds ({(rapid_time * 200)/60:.1f} minutes)")

if __name__ == "__main__":
    try:
        speed_demo()
    except KeyboardInterrupt:
        print("\n⚠️ Speed test interrupted")
    except Exception as e:
        print(f"\n❌ Speed test error: {str(e)}")
