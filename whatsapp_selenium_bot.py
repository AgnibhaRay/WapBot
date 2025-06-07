#!/usr/bin/env python3
"""
WhatsApp Bot using Selenium - ULTRA-FAST SPEED OPTIMIZED ⚡

Created by: Agnibha Ray (@agnibharay)
Project: WapBot - Ultra-Fast WhatsApp Automation
Performance: 200x speed optimization achieved

This bot automates WhatsApp Web using advanced Selenium browser automation
with intelligent caching, optimized Chrome settings, and multiple speed modes.

Features:
- Rapid Fire Mode: 0.05s delays (200x faster!)
- Smart element caching for lightning-fast performance
- Optimized Chrome browser settings
- Multiple speed modes (Normal, Fast, Rapid Fire, Custom)
- Robust error handling and recovery
- Real-time feedback and progress tracking

Use responsibly and respect WhatsApp's terms of service.
"""

import time
import random
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse

class WhatsAppSeleniumBot:
    def __init__(self, headless=False, fast_mode=True):
        """
        Initialize the WhatsApp bot with Selenium WebDriver
        
        Args:
            headless (bool): Run browser in headless mode (no GUI)
            fast_mode (bool): Enable fast mode with optimized settings
        """
        self.driver = None
        self.wait = None
        self.fast_wait = None
        self.headless = headless
        self.fast_mode = fast_mode
        self.message_box = None  # Cache the message box element
        
        self.messages = [
            "Hey! Uthja Kale Kawa!(AI generated) [Message Powered by WapBot by Agnibha ray]",
            "Hey! Uthja Kale Kawa! [Message Powered by WapBot by Agnibha ray]",
            "Hey! Uthja Kale Kawa! (AI generated) [Message Powered by WapBot by Agnibha ray]",
            "Hey! Uthja Kale Kawa! (AI generated) [Message Powered by WapBot by Agnibha ray]",
            "Bhen di fuddi hai! [Message Powered by WapBot by Agnibha ray]",
            "Sigma sigma boy! [Message Powered by WapBot by Agnibha ray]",
            "Kya scene hai? [Message Powered by WapBot by Agnibha ray]",
            "Pechkash paglu! [Message Powered by WapBot by Agnibha ray]",
            "Please Please Mukjhe maat maaro! [Message Powered by WapBot by Agnibha ray]",
            "Mujhe Jeena hai! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maroing! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat marobest! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat marold brighter! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro amazing! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maro energy! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat maroe! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat marois going well! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat marorighten your day! [Message Powered by WapBot by Agnibha ray]",
            "Sadda Modi Balle Balle!! Please mujhe maat marorful person! [Message Powered by WapBot by Agnibha ray]"
        ]
    
    def setup_driver(self):
        """Setup and configure the Chrome WebDriver with speed optimizations"""
        try:
            chrome_options = Options()
            
            if self.headless:
                chrome_options.add_argument("--headless")
            
            # Speed optimization flags
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage") 
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--disable-extensions")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-popup-blocking")
            chrome_options.add_argument("--disable-web-security")
            chrome_options.add_argument("--disable-features=VizDisplayCompositor")
            chrome_options.add_argument("--disable-background-timer-throttling")
            chrome_options.add_argument("--disable-backgrounding-occluded-windows")
            chrome_options.add_argument("--disable-renderer-backgrounding")
            chrome_options.add_argument("--disable-field-trial-config")
            chrome_options.add_argument("--disable-background-networking")
            chrome_options.add_argument("--disable-sync")
            chrome_options.add_argument("--disable-translate")
            chrome_options.add_argument("--disable-ipc-flooding-protection")
            chrome_options.add_argument("--disable-hang-monitor")
            chrome_options.add_argument("--disable-client-side-phishing-detection")
            chrome_options.add_argument("--disable-component-update")
            chrome_options.add_argument("--disable-default-apps")
            chrome_options.add_argument("--disable-domain-reliability")
            chrome_options.add_argument("--disable-features=TranslateUI")
            chrome_options.add_argument("--disable-fetching-hints-at-navigation-start")
            chrome_options.add_argument("--disable-logging")
            chrome_options.add_argument("--disable-login-animations")
            chrome_options.add_argument("--disable-new-avatar-menu")
            chrome_options.add_argument("--disable-new-profile-management")
            chrome_options.add_argument("--disable-plugins")
            chrome_options.add_argument("--disable-profile-finder")
            chrome_options.add_argument("--disable-save-password-bubble")
            
            # Performance preferences
            prefs = {
                "profile.default_content_setting_values": {
                    "images": 2,  # Block images for faster loading
                    "plugins": 2,
                    "popups": 2,
                    "geolocation": 2,
                    "notifications": 2,
                    "media_stream": 2,
                },
                "profile.managed_default_content_settings": {
                    "images": 2
                }
            }
            chrome_options.add_experimental_option("prefs", prefs)
            
            # Set user agent
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
            
            # Try multiple approaches to setup ChromeDriver
            service = None
            
            # First, try system-installed ChromeDriver (most reliable)
            if not self.fast_mode:
                print("🔍 Looking for system ChromeDriver...")
            common_paths = [
                "/opt/homebrew/bin/chromedriver",  # Homebrew on Apple Silicon
                "/usr/local/bin/chromedriver",     # Homebrew on Intel
                "/usr/bin/chromedriver",           # System install
                "chromedriver"                     # In PATH
            ]
            
            for path in common_paths:
                try:
                    import os
                    # Check if file exists and is executable
                    if path != "chromedriver" and not os.path.isfile(path):
                        continue
                        
                    if not self.fast_mode:
                        print(f"🧪 Testing ChromeDriver at: {path}")
                    test_service = Service(path)
                    test_driver = webdriver.Chrome(service=test_service, options=chrome_options)
                    test_driver.quit()
                    service = test_service
                    if not self.fast_mode:
                        print(f"✅ Found working ChromeDriver at: {path}")
                    break
                except Exception as test_e:
                    if not self.fast_mode:
                        print(f"   ❌ Failed: {str(test_e)}")
                    continue
            
            # If system ChromeDriver not found, try webdriver-manager
            if not service:
                try:
                    if not self.fast_mode:
                        print("🔧 Attempting to download ChromeDriver...")
                        print("🧹 Clearing ChromeDriver cache...")
                    
                    # Clear any cached driver data that might be corrupted
                    cache_dir = os.path.expanduser("~/.wdm")
                    if os.path.exists(cache_dir):
                        shutil.rmtree(cache_dir, ignore_errors=True)
                    
                    # Download ChromeDriver
                    from webdriver_manager.chrome import ChromeDriverManager
                    driver_path = ChromeDriverManager().install()
                    
                    # Fix the common issue where webdriver-manager returns wrong file path
                    if not os.path.isfile(driver_path) or "THIRD_PARTY_NOTICES" in driver_path or not os.access(driver_path, os.X_OK):
                        if not self.fast_mode:
                            print(f"🔍 Fixing ChromeDriver path (was: {driver_path})")
                        # Find the actual chromedriver binary in the directory
                        driver_dir = os.path.dirname(driver_path)
                        
                        # First check the same directory
                        chromedriver_path = os.path.join(driver_dir, "chromedriver")
                        if os.path.isfile(chromedriver_path):
                            driver_path = chromedriver_path
                            if not self.fast_mode:
                                print(f"✅ Found actual ChromeDriver: {driver_path}")
                        else:
                            # Look for chromedriver binary in the entire .wdm tree
                            wdm_root = os.path.expanduser("~/.wdm")
                            found = False
                            for root, dirs, files in os.walk(wdm_root):
                                if "chromedriver" in files:
                                    potential_path = os.path.join(root, "chromedriver")
                                    if os.access(potential_path, os.X_OK):
                                        driver_path = potential_path
                                        if not self.fast_mode:
                                            print(f"✅ Found actual ChromeDriver: {driver_path}")
                                        found = True
                                        break
                            
                            if not found:
                                raise Exception("Could not locate executable chromedriver binary")
                    
                    # Make sure the driver is executable
                    os.chmod(driver_path, 0o755)
                    
                    service = Service(driver_path)
                    if not self.fast_mode:
                        print(f"✅ Downloaded ChromeDriver: {driver_path}")
                    
                except Exception as download_e:
                    if not self.fast_mode:
                        print(f"⚠️ Auto-download failed: {str(download_e)}")
            
            if not service:
                raise Exception("Could not find or setup ChromeDriver. Please install manually with 'brew install chromedriver'")
            
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            if not self.headless:
                self.driver.maximize_window()
            
            # Fast mode uses shorter timeouts
            timeout = 5 if self.fast_mode else 30
            self.wait = WebDriverWait(self.driver, timeout)
            self.fast_wait = WebDriverWait(self.driver, 2)  # Ultra-fast wait for cached elements
            
            if not self.fast_mode:
                print("✅ Chrome WebDriver initialized successfully!")
            return True
            
        except Exception as e:
            print(f"❌ Error setting up WebDriver: {str(e)}")
            if not self.fast_mode:
                print("\n🔧 Troubleshooting steps:")
                print("1. Install Chrome browser if not already installed")
                print("2. Install ChromeDriver manually:")
                print("   brew install chromedriver")
                print("   brew install --cask chromedriver")
                print("3. Allow ChromeDriver in Security & Privacy if on macOS")
                print("4. Or run the manual installer: ./install_chromedriver.sh")
            return False
    
    def login_to_whatsapp(self):
        """Navigate to WhatsApp Web and wait for user to scan QR code - OPTIMIZED"""
        try:
            if not self.fast_mode:
                print("🌐 Opening WhatsApp Web...")
            
            # Add cache control headers to speed up loading
            self.driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            })
            
            self.driver.get("https://web.whatsapp.com")
            
            # Fast loading optimization
            if self.fast_mode:
                # Don't wait for all images to load, just the essential elements
                self.driver.execute_script("window.stop();")
            
            # Wait for page to load with faster timeout in fast mode
            time.sleep(5)
            
            # Check if QR code is present
            print("🔍 Checking for QR code...")
            qr_selectors = [
                '[data-testid="qr-code"]',
                'canvas[aria-label="Scan me!"]',
                'div[data-ref]',  # QR code container
                'canvas'
            ]
            
            qr_found = False
            for selector in qr_selectors:
                try:
                    qr_element = self.driver.find_element(By.CSS_SELECTOR, selector)
                    if qr_element.is_displayed():
                        qr_found = True
                        print("📱 QR code found! Please scan with your phone...")
                        break
                except:
                    continue
            
            if not qr_found:
                # Check if already logged in
                print("🔍 Checking if already logged in...")
                login_indicators = [
                    '[data-testid="chat-list"]',
                    '[data-testid="search"]',
                    'div[data-testid="chat-list-search"]',
                    '[aria-label="Search input textbox"]',
                    'div[data-testid="side"]'
                ]
                
                for selector in login_indicators:
                    try:
                        element = self.driver.find_element(By.CSS_SELECTOR, selector)
                        if element.is_displayed():
                            print("✅ Already logged in to WhatsApp Web!")
                            time.sleep(3)
                            return True
                    except:
                        continue
                        
                print("⚠️ Neither QR code nor login interface found. Continuing anyway...")
            
            print("⏳ Waiting for login (up to 120 seconds)...")
            print("💡 Tip: The QR code refreshes every 20 seconds, so scan quickly!")
            
            # Extended wait with progress indicators
            start_time = time.time()
            max_wait_time = 120  # 2 minutes
            
            while time.time() - start_time < max_wait_time:
                try:
                    # Check for successful login indicators
                    success_selectors = [
                        '[data-testid="chat-list"]',
                        '[data-testid="search"]', 
                        'div[data-testid="chat-list-search"]',
                        '[aria-label="Search input textbox"]',
                        'div[data-testid="side"]',
                        'div[data-testid="conversation-compose-box-input"]'
                    ]
                    
                    for selector in success_selectors:
                        try:
                            element = WebDriverWait(self.driver, 2).until(
                                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                            )
                            if element.is_displayed():
                                print("✅ Successfully logged in to WhatsApp Web!")
                                time.sleep(5)  # Let the interface fully load
                                return True
                        except:
                            continue
                    
                    # Show progress every 15 seconds
                    elapsed = int(time.time() - start_time)
                    if elapsed % 15 == 0 and elapsed > 0:
                        remaining = max_wait_time - elapsed
                        print(f"⏳ Still waiting... {remaining} seconds remaining")
                    
                    time.sleep(1)
                    
                except Exception as check_e:
                    print(f"⚠️ Check error: {str(check_e)}")
                    time.sleep(2)
                    continue
            
            print("❌ Login timeout. Please try again and scan the QR code more quickly.")
            print("💡 Tips:")
            print("   - Make sure WhatsApp is installed on your phone")
            print("   - Open WhatsApp > Settings > Linked Devices > Link a Device")
            print("   - Scan the QR code within 20 seconds")
            return False
                
        except Exception as e:
            print(f"❌ Error during login: {str(e)}")
            return False
    
    def find_contact(self, contact_name_or_number):
        """Find and open a chat with the specified contact - OPTIMIZED"""
        try:
            if not self.fast_mode:
                print(f"🔍 Searching for contact: {contact_name_or_number}")
            
            # Use faster waits in fast mode
            wait_time = self.fast_wait if self.fast_mode else self.wait
            
            # Find the search box with optimized selectors (most common first)
            search_selectors = [
                '[data-testid="search"]',
                'div[contenteditable="true"][data-tab="3"]',
                '[data-testid="chat-list-search"]',
                'div[title="Search input textbox"]'
            ]
            
            search_box = None
            for selector in search_selectors:
                try:
                    search_box = wait_time.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                    break
                except TimeoutException:
                    continue
            
            if not search_box:
                if not self.fast_mode:
                    print("❌ Could not find search box")
                return False
            
            # Fast typing with ActionChains for better performance
            actions = ActionChains(self.driver)
            
            # Click and clear the search box
            actions.click(search_box).perform()
            
            # Clear with keyboard shortcut (faster than .clear())
            actions.key_down(Keys.COMMAND if 'Darwin' in os.uname().sysname else Keys.CONTROL).send_keys('a').key_up(Keys.COMMAND if 'Darwin' in os.uname().sysname else Keys.CONTROL).perform()
            
            # Fast delay in fast mode
            delay = 0.2 if self.fast_mode else 1
            time.sleep(delay)
            
            # Type the contact name/number with faster typing
            actions.send_keys(contact_name_or_number).perform()
            
            # Shorter wait for search results in fast mode
            search_delay = 0.5 if self.fast_mode else 2
            time.sleep(search_delay)
            
            # Optimized contact search - try exact match first
            contact_selectors = [
                f'span[title="{contact_name_or_number}"]',  # Exact match first
                f'span[title*="{contact_name_or_number}"]', # Partial match
                '[data-testid="cell-frame-container"]',     # Generic containers
                'div[data-testid="chat-list"] > div'        # Chat list items
            ]
            
            contact_found = False
            for selector in contact_selectors:
                try:
                    # Use faster find method in fast mode
                    if self.fast_mode:
                        contacts = self.driver.find_elements(By.CSS_SELECTOR, selector)
                    else:
                        contacts = wait_time.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
                    
                    for contact in contacts[:3]:  # Only check first 3 results for speed
                        try:
                            if contact_name_or_number.lower() in contact.text.lower():
                                actions.click(contact).perform()
                                contact_found = True
                                break
                        except:
                            continue
                    if contact_found:
                        break
                except:
                    continue
            
            if not contact_found:
                # Try clicking the first search result
                try:
                    first_result = self.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="cell-frame-container"]'))
                    )
                    first_result.click()
                    contact_found = True
                except:
                    pass
            
            if contact_found:
                print(f"✅ Found and opened chat with: {contact_name_or_number}")
                time.sleep(2)
                return True
            else:
                print(f"❌ Could not find contact: {contact_name_or_number}")
                return False
                
        except Exception as e:
            print(f"❌ Error finding contact: {str(e)}")
            return False
    
    def send_message(self, message):
        """Send a single message in the current chat - ULTRA OPTIMIZED"""
        try:
            # Clean message of problematic Unicode characters (minimal processing)
            cleaned_message = message.encode('ascii', 'ignore').decode('ascii')
            if not cleaned_message.strip():
                cleaned_message = "Hello! This is a message from the WhatsApp bot."
            
            # Use cached message box if available (MASSIVE speed boost)
            if self.message_box is not None:
                try:
                    # Test if cached element is still valid
                    self.message_box.is_displayed()
                    message_box = self.message_box
                except:
                    # Cache invalid, need to find again
                    self.message_box = None
                    message_box = None
            else:
                message_box = None
            
            # Find message box only if not cached
            if message_box is None:
                input_selectors = [
                    '[data-testid="conversation-compose-box-input"]',  # Most common
                    'div[contenteditable="true"][data-tab="10"]',
                    'div[contenteditable="true"][data-tab="1"]',
                    'div[role="textbox"]'
                ]
                
                wait_time = self.fast_wait if self.fast_mode else self.wait
                
                for selector in input_selectors:
                    try:
                        message_box = wait_time.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                        # Cache the message box for future use
                        self.message_box = message_box
                        break
                    except TimeoutException:
                        continue
                
                if not message_box:
                    if not self.fast_mode:
                        print("❌ Could not find message input box")
                    return False
            
            # Ultra-fast message sending with ActionChains
            actions = ActionChains(self.driver)
            
            # Single action chain for maximum speed
            actions.click(message_box)
            
            # Skip delays in fast mode
            if not self.fast_mode:
                time.sleep(0.1)
            
            # Fast clear and type
            actions.key_down(Keys.COMMAND if 'Darwin' in os.uname().sysname else Keys.CONTROL)
            actions.send_keys('a')
            actions.key_up(Keys.COMMAND if 'Darwin' in os.uname().sysname else Keys.CONTROL)
            actions.send_keys(cleaned_message)
            actions.send_keys(Keys.RETURN)
            
            # Execute all actions at once
            actions.perform()
            
            # Minimal delay - only wait if not in fast mode
            if self.fast_mode:
                time.sleep(0.1)  # Just enough to register the send
            else:
                time.sleep(0.5)
            
            return True
            
        except Exception as e:
            if not self.fast_mode:
                print(f"❌ Error sending message: {str(e)}")
            # Reset cache on error
            self.message_box = None
            return False
    
    def send_multiple_messages(self, contact, num_messages=1000, delay_seconds=30):
        """
        Send multiple messages to a contact - ULTRA OPTIMIZED FOR SPEED
        
        Args:
            contact (str): Contact name or phone number
            num_messages (int): Number of messages to send
            delay_seconds (int): Delay between messages in seconds (0.1-30)
        """
        try:
            # Speed optimization: reduce delay for fast mode
            if self.fast_mode and delay_seconds > 5:
                original_delay = delay_seconds
                delay_seconds = max(0.1, delay_seconds / 10)  # 10x faster
                print(f"⚡ FAST MODE: Reduced delay from {original_delay}s to {delay_seconds}s")
            
            if not self.fast_mode:
                print(f"🚀 Starting to send {num_messages} messages to {contact}")
                print(f"⏱️ Delay between messages: {delay_seconds} seconds")
            else:
                print(f"⚡ ULTRA-FAST: Sending {num_messages} messages with {delay_seconds}s delay")
            
            # Setup driver and login
            if not self.setup_driver():
                return False
            
            if not self.login_to_whatsapp():
                return False
            
            # Find the contact
            if not self.find_contact(contact):
                return False
            
            successful_messages = 0
            failed_messages = 0
            start_time = time.time()
            
            if not self.fast_mode:
                print(f"\n📱 Starting to send messages...")
            else:
                print(f"⚡ RAPID FIRE MODE: Sending messages at maximum speed...")
            
            # Pre-calculate message pattern for speed
            message_cycle = len(self.messages)
            
            for i in range(num_messages):
                try:
                    # Optimized message selection (no random for speed)
                    if i < message_cycle:
                        message = self.messages[i]
                    else:
                        message = self.messages[i % message_cycle]
                    
                    # Reduced logging in fast mode
                    if not self.fast_mode or i % 50 == 0:  # Log every 50th message in fast mode
                        if self.fast_mode:
                            elapsed = time.time() - start_time
                            rate = (i + 1) / elapsed if elapsed > 0 else 0
                            print(f"⚡ Messages {i+1}/{num_messages} | Rate: {rate:.1f} msg/sec")
                        else:
                            print(f"📤 Sending message {i+1}/{num_messages}: {message[:50]}...")
                    
                    if self.send_message(message):
                        successful_messages += 1
                        if not self.fast_mode:
                            print(f"✅ Message {i+1} sent successfully!")
                    else:
                        failed_messages += 1
                        if not self.fast_mode:
                            print(f"❌ Failed to send message {i+1}")
                    
                    # Optimized delay handling
                    if i < num_messages - 1:
                        if self.fast_mode:
                            # Ultra-fast mode: minimal delay
                            if delay_seconds >= 0.1:
                                time.sleep(delay_seconds)
                            # For delays < 0.1, no sleep to maximize speed
                        else:
                            if not self.fast_mode:
                                print(f"⏳ Waiting {delay_seconds} seconds before next message...")
                            time.sleep(delay_seconds)
                    
                except KeyboardInterrupt:
                    print("\n⚠️ Bot stopped by user")
                    break
                except Exception as e:
                    failed_messages += 1
                    print(f"❌ Error sending message {i+1}: {str(e)}")
                    continue
            
            print(f"\n📊 Summary:")
            print(f"✅ Successful messages: {successful_messages}")
            print(f"❌ Failed messages: {failed_messages}")
            print(f"📱 Total attempted: {successful_messages + failed_messages}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error in send_multiple_messages: {str(e)}")
            return False
        finally:
            self.close()
    
    def send_rapid_fire_messages(self, contact, num_messages=1000):
        """
        Send messages in rapid-fire mode with minimal delays - MAXIMUM SPEED
        
        Args:
            contact (str): Contact name or phone number
            num_messages (int): Number of messages to send
        """
        print(f"🔥 RAPID FIRE MODE: Sending {num_messages} messages at MAXIMUM SPEED")
        print("⚠️  WARNING: This will send messages as fast as possible!")
        print("💡 Tip: WhatsApp may rate-limit if too fast. Use with caution.")
        
        # Force fast mode settings
        original_fast_mode = self.fast_mode
        self.fast_mode = True
        
        try:
            result = self.send_multiple_messages(contact, num_messages, delay_seconds=0.05)
            return result
        finally:
            # Restore original fast mode setting
            self.fast_mode = original_fast_mode

    def close(self):
        """Close the browser and clean up"""
        if self.driver:
            print("🔒 Closing browser...")
            self.driver.quit()

def main():
    print("🤖 WhatsApp Bot with Selenium - SPEED OPTIMIZED")
    print("=" * 45)
    print()
    
    # Get contact information
    contact = input("Enter contact name or phone number (e.g., 'John Doe' or '+1234567890'): ").strip()
    
    if not contact:
        print("❌ Contact name/number is required")
        return
    
    # Get number of messages
    try:
        num_messages = int(input("Enter number of messages to send (default 1000): ") or "1000")
        if num_messages <= 0:
            print("❌ Number of messages must be positive")
            return
    except ValueError:
        print("❌ Please enter a valid number")
        return
    
    # Speed mode selection
    print("\n🚀 Speed Mode Options:")
    print("1. Normal Mode (30s delays) - Safe and reliable")
    print("2. Fast Mode (3s delays) - 10x faster")
    print("3. Rapid Fire (0.05s delays) - MAXIMUM SPEED ⚡")
    print("4. Custom delay")
    
    try:
        speed_choice = input("Choose speed mode (1-4, default 2): ").strip() or "2"
        
        if speed_choice == "1":
            delay_seconds = 30
            fast_mode = False
            mode_name = "Normal"
        elif speed_choice == "2":
            delay_seconds = 3
            fast_mode = True
            mode_name = "Fast"
        elif speed_choice == "3":
            delay_seconds = 0.05
            fast_mode = True
            mode_name = "Rapid Fire ⚡"
        elif speed_choice == "4":
            delay_seconds = float(input("Enter custom delay in seconds (0.05-300): ") or "3")
            if delay_seconds < 0.05:
                delay_seconds = 0.05
            elif delay_seconds > 300:
                delay_seconds = 300
            fast_mode = delay_seconds <= 5
            mode_name = f"Custom ({delay_seconds}s)"
        else:
            delay_seconds = 3
            fast_mode = True
            mode_name = "Fast (default)"
            
    except ValueError:
        print("❌ Invalid input, using default Fast mode")
        delay_seconds = 3
        fast_mode = True
        mode_name = "Fast (default)"
    
    # Calculate estimated time
    if delay_seconds >= 1:
        est_time_min = (num_messages * delay_seconds) // 60
        est_time_sec = (num_messages * delay_seconds) % 60
        time_estimate = f"{est_time_min}m {est_time_sec}s" if est_time_min > 0 else f"{est_time_sec}s"
    else:
        total_seconds = num_messages * delay_seconds
        if total_seconds < 60:
            time_estimate = f"{total_seconds:.1f}s"
        else:
            time_estimate = f"{total_seconds/60:.1f}m"
    
    # Confirm before starting
    print(f"\n📋 Configuration:")
    print(f"👤 Contact: {contact}")
    print(f"📱 Messages: {num_messages}")
    print(f"🚀 Mode: {mode_name}")
    print(f"⏱️ Delay: {delay_seconds}s per message")
    print(f"⏰ Estimated time: {time_estimate}")
    print()
    print("⚠️ Important:")
    print("- Keep your computer awake during the process")
    print("- Don't close the browser window")
    print("- Use responsibly and with recipient's consent")
    
    if delay_seconds < 1:
        print("⚠️ SPEED WARNING: Very fast messaging may trigger WhatsApp rate limits!")
    
    print()
    
    confirm = input("Continue? (y/n): ").lower().strip()
    
    if confirm != 'y':
        print("❌ Operation cancelled")
        return
    
    # Create and run the bot with optimized settings
    print(f"\n🤖 Initializing bot in {mode_name} mode...")
    bot = WhatsAppSeleniumBot(headless=False, fast_mode=fast_mode)
    
    try:
        if delay_seconds <= 0.1:
            # Use rapid fire method for ultra-fast messaging
            bot.send_rapid_fire_messages(contact, num_messages)
        else:
            # Use standard optimized method
            bot.send_multiple_messages(contact, num_messages, delay_seconds)
    except KeyboardInterrupt:
        print("\n⚠️ Bot stopped by user (Ctrl+C)")
    except Exception as e:
        print(f"\n❌ Bot error: {str(e)}")
    finally:
        print("\n🏁 Bot session completed!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"\n💥 Unexpected error: {str(e)}")
