from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver

driver.get("https://www.douglas.ro/")

search_box = driver.find_element(By.NAME, "//input[@type='search']")
search_box.send_keys("DIOR Forever No-Transfer 24h Wear Matte Foundation")
search_box.send_keys(Keys.ENTER)
search_box.find_element(By.XPATH, '//*[@id="productDetailPageBuyProductForm"]/div/div/button')
search_box.send_keys(Keys.ENTER)

driver.quit()