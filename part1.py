import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.google.com")
loc1= driver.find_element(By.CLASS_NAME,'gLFyf')
loc1.send_keys("Selenium")
loc1.send_keys(Keys.ENTER)
time.sleep(10)
loc2= driver.find_element(By.XPATH,"/html/body/div[6]/div/div[11]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a/h3").click()
time.sleep(10)

