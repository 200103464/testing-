import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
time.sleep(5)
loc1= driver.find_element(By.NAME,"email")
loc1.send_keys("200103464@stu.sdu.edu.kz")
loc2= driver.find_element(By.ID,"pass")
loc2.send_keys("200103464")
time.sleep(6)
loc3= driver.find_element(By.NAME,'login').click()

time.sleep(10)