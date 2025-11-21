from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time



PROXY = "sandbox-proxy:8080"

chrome_options = Options()
chrome_options.add_argument(f'--proxy-server={PROXY}')
chrome_options.add_argument('--ignore-certificate-errors')

print(f"--- Connecting to Isolated Browser via Proxy {PROXY} ---")



driver = webdriver.Remote(
    command_executor='http://sandbox-browser:4444/wd/hub',
    options=chrome_options
)

try:
    print("Browser Connected! Attempting to visit Example.com...")
    driver.get("http://example.com")
    print(f"Success! Page Title: {driver.title}")
    print("Traffic has been logged to the 'logger' container.")
    time.sleep(5)
except Exception as e:
    print(f"Error: {e}")
finally:
    
    driver.quit()
    print("Session Closed & Reset.")