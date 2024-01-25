from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_page


class Login_page(Base_page):
	USERNAME = (By.XPATH, "//input[@id='loginMail']")
	PASSWORD = (By.XPATH, "//input[@id='loginpasswordfield']")
	LOGIN_BUTTON = (By.CSS_SELECTOR, "'//div[@class='login-submit']")
	LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, 'div.douglas-login-error i + p')
	ACCEPT_BUTTON = (By.XPATH, '//button[@data-testid="uc-accept-all-button"]')


	def accept_cookies(self):
		try:
			shadow_element = Shadow(self.chrome)
			shadow_element.get_shadow_element(*self.ACCEPT_BUTTON)
		except:
			pass

	def insert_username(self, user_name="email_for_tests@yahoo.com"):
		username = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.USERNAME))
		username.send_keys(user_name)

	def insert_password(self, user_password="12345678"):
		password = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.PASSWORD))
		password.send_keys(user_password)

	def click_login_button(self):
		self.chrome.find_element(*self.LOGIN_BUTTON).click()

	def check_current_url(self):
		actual_url = self.chrome.current_url
		expected_url = 'https://www.douglas.ro/account'
		assert expected_url == actual_url, "The url is incorrect. Please check the login functionality"

	def check_login_error_message(self, expected_error_message):
		self.check_error_message(*self.LOGIN_ERROR_MESSAGE, expected_error_message)

	# self.check_error_message(By.CSS_SELECTOR,'div.douglas-login-error i + p',expected_error_message)

	def check_error_message(self, by, selector, expected_error_message):
		error_message_web_element = WebDriverWait(self.chrome, 10).until(
			EC.presence_of_element_located(self.LOGIN_ERROR_MESSAGE))
		actual_error_message_text = error_message_web_element.text

		assert expected_error_message == actual_error_message_text, f'Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}'

	presence_of_element_located((By.CSS_SELECTOR, 'div.douglas-login-error i + p'))
