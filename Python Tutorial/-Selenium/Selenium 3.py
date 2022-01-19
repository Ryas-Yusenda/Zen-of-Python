from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PATH = "../chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.techwithtim.net/tutorials/python-programming/")

link = driver.find_element_by_link_text("Beginner Python Tutorials")
link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.ID, "sow-button-19310003"))
    )
    element.click()

   #  driver.back()
   #  driver.back()
   #  driver.back()
   #  driver.forward()
   #  driver.forward()

except:
    driver.quit()
