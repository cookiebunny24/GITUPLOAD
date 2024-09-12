from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get("https://www.reddit.com/")