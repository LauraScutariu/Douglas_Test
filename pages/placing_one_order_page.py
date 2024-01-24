from pyshadow.main import Shadow
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from pages.base_page import Base_page

class Home_page(Base_page):
	def accept_cookies(self):
		try:
			shadow_element = Shadow(self.chrome)
			shadow_element.get_shadow_element(*self.ACCEPT_BUTTON)
		except:
			pass

	LOGIN_TO_THE_APPLICATION = ("https://www.douglas.ro/account")
	SEARCH_BOX = (By.NAME, "//input[@type='search']")
	ADD_IN_SHOPPING_CART = (By.XPATH, "//input[@id='personalFirstName']")
	CHECK_OUT = (By.XPATH, "//a[@id='begin-checkout-btn']")
	ACCEPT_CONDITIONS = (By.CSS_SELECTOR, "//label[@class='checkout-confirm-tos-label custom-control-label']")
	PLACE_ORDER = (By.XPATH, "//button[@id='confirmFormSubmit']")
	def login_to_the_application(self):
				account_dropdown = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.ACCOUNT_DROPDOWN))
				account_dropdown.click()
				self.chrome.find_element(*self.LOGIN_LINK).click()

	def search_box(self):
		search_box = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.SEARCH_BOX))
		search_box.send_keys(search_box)

	def add_in_shopping_cart(self):
		add_in_shopping_cart = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.ADD_IN_SHOPPING_CART))
		add_in_shopping_cart.send_keys(add_in_shopping_cart)

	def check_out(self):
		check_out = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.CHECK_OUT))
		check_out.send_keys(check_out)

	def accept_conditions(self):
		accept_conditions = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.ACCEPT_CONDITIONS))
		accept_conditions.send_keys(accept_conditions)

	def place_order(self):
		place_order = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.PLACE_ORDER))
		place_order.send_keys(place_order)