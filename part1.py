import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.google.com")
loc1= driver.find_element(By.CLASS_NAME,'gLFyf')
loc1.send_keys("Selenium")
loc1.send_keys(Keys.ENTER)
time.sleep(5)
loc2= driver.find_element(By.XPATH,"//*[contains(@class,'iUh30 tjvcx')]").click()
time.sleep(5)

