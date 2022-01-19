# https://sites.google.com/a/chromium.org/chromedriver/downloads
from selenium import webdriver

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net")
print(driver.title)
driver.quit()
