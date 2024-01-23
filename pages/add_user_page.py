from selenium import webdriver
from selenium.webdriver.common.keys import Keys

webdriver_path = '/path/to/chromedriver'

driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get('https://douglas.ro')

username_input = driver.find_element('01', 'Laura')
password_input = driver.find_element('02', '12345678')
submit_button = driver.find_element('03', 'submit')

username_input.send_keys('Laura')
password_input.send_keys('12345678')
submit_button.click()

driver.implicitly_wait(6)

driver.quit()