from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "../chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(5)

cookie = driver.find_elements_by_id("bigCookie")
cookie_count = driver.find_elements_by_id("cookies")
items = [driver.find_elements_by_id(
    "productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click()

for i in range(5000):
    actions.perform()
