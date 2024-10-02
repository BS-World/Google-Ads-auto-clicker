from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Path to the Edge WebDriver
EDGE_DRIVER_PATH = 'D:/Driver_Notes/msedgedriver.exe'

# List of URLs to visit
urls = [
    "https://www.youtube.com/@CartoonHUB-r1f",
    "https://www.youtube.com/@CartoonHUB-r1f",
    "https://www.youtube.com/@CartoonHUB-r1f",
    "https://www.youtube.com/@CartoonHUB-r1f",
    "https://www.youtube.com/@CartoonHUB-r1f",
    "https://www.youtube.com/@CartoonHUB-r1f"
]

# User-Agent strings to mimic different browsers
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/53.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/16.16299"
]

def visit_site():
    service = Service(EDGE_DRIVER_PATH)
    options = webdriver.EdgeOptions()
    options.add_argument(f"user-agent={random.choice(user_agents)}")  # Add random user-agent
    driver = webdriver.Edge(service=service, options=options)

    url = random.choice(urls)
    
    try:
        driver.get(url)
        print(f"Visited {url}")

        # Wait for the page to load
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Look for ad containers
        ad_elements = driver.find_elements(By.CSS_SELECTOR, 'iframe[src*="googleads"]')
        print(f"Found {len(ad_elements)} ad containers.")

        for ad_element in ad_elements:
            try:
                driver.switch_to.frame(ad_element)  # Switch to the ad iframe
                clickable_ads = driver.find_elements(By.CSS_SELECTOR, 'a[href*="googleadservices.com"], a[href*="doubleclick.net"]')
                print(f"Found {len(clickable_ads)} clickable ads.")

                for ad in clickable_ads:
                    try:
                        ad.click()
                        print(f"Clicked on ad: {ad.get_attribute('href')}")
                        time.sleep(random.uniform(1, 3))  # Wait between clicks
                    except Exception as click_error:
                        print(f"Error clicking ad: {click_error}")
                
                driver.switch_to.default_content()  # Switch back to the main content
            except Exception as frame_error:
                print(f"Error processing ad iframe: {frame_error}")

        # Slowly scroll down the page
        scroll_pause_time = 0.5
        screen_height = driver.execute_script("return window.innerHeight;")
        scroll_height = driver.execute_script("return document.body.scrollHeight;")

        for i in range(0, scroll_height, screen_height):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(scroll_pause_time)

        # Random wait before finishing
        time.sleep(random.uniform(1, 5))

    except Exception as e:
        print(f"Error visiting {url}: {e}")

    finally:
        driver.quit()

def generate_traffic(visitors=1000):
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(visit_site) for _ in range(visitors)]
        for future in futures:
            future.result()  # Wait for all threads to finish

if __name__ == "__main__":
    generate_traffic()
