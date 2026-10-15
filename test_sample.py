from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# --- Unit Tests ---
def add(a, b):
    return a + b

def test_addition():
    assert add(2, 3) == 5

def test_subtraction():
    assert (5 - 3) == 2

# --- Selenium Web Test ---
def test_selenium_example():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Background mode for CI
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://example.com")
    
    assert "Example Domain" in driver.title
    driver.quit()