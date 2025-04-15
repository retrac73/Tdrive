
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

def search_tdrive():
    chromedriver_autoinstaller.install()  # Automatically installs the right ChromeDriver

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.gnc.com/")
    time.sleep(3)

    try:
        search_input = driver.find_element(By.ID, "search-input")
        search_input.clear()
        search_input.send_keys("T-Drive")
        search_input.send_keys(Keys.RETURN)
        time.sleep(5)

        no_results = driver.find_elements(By.CLASS_NAME, "search-no-results-message")
        if no_results:
            print("Still no T-Drive...")
        else:
            print("T-Drive FOUND!")
            # You could trigger a webhook or email alert here
    except Exception as e:
        print("Error:", e)
    finally:
        driver.quit()

search_tdrive()
