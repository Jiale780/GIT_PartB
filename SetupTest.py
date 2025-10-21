from selenium import webdriver

# --- Configuration ---
URL = "https://practice.qabrains.com/"

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)  # Implicit wait for 10 seconds
    driver.get(URL)
    return driver

