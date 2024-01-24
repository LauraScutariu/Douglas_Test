# import driver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# driver.get("https://www.douglas.ro/")
#
# time.sleep(3)
#
# try:
#     accept_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]")
#     accept_button.click()
#
#     time.sleep(3)
#
# #try:
#     login_button = driver.find_element(By.CLASS_NAME, "login-button")
#     login_button.click()
#
#     time.sleep(5)
#
#     username_field = driver.find_element(By.NAME, "username")
#     password_field = driver.find_element(By.NAME, "password")
#
#     username_field.send_keys("test_for_emails@yahoo.com")
#     password_field.send_keys("12345678")
#
#     submit_button = driver.find_element(By.NAME, "submit_button")
#     submit_button.click()
#
#     time.sleep(5)
#
#     assert "My Account" in driver.page_source
#
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
#
# finally:
#
#     driver.quit()