import time

import self
from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Base_page


class Home_page(Base_page):
	CLIENT_TYPE = (By.CSS_SELECTOR, "//div[@class='e-custom-select__trigger']")
	CLIENT_GEN = (By.CSS_SELECTOR, "//span[@class='text']")
	FIRSTNAME = (By.XPATH, "//input[@id='personalFirstName']")
	NAME = (By.XPATH, "//input[@id='personalLastName']")
	EMAIL = (By.XPATH, "//input[@id='personalMail']")
	PASSWORD = (By.XPATH, "//input[@id='personalPassword']")
	# ADDRESS
	STREET_AND_NUMBER = (By.XPATH, "//input[@id='billingAddressAddressStreet']")
	BLOCK = (By.XPATH, "//input[@id='billingAddressadditionaladdressfields_block']")
	SCALE = (By.XPATH, "///input[@id='billingAddressadditionaladdressfields_entrance']")
	FLOOR = (By.XPATH, "//input[@id='billingAddressadditionaladdressfields_floor']")
	HOUSE_NUMBER = (By.XPATH, "//input[@id='billingAddressadditionaladdressfields_apartment']")
	SECTOR = (By.CSS_SELECTOR, "//div[@class='e-custom-select__trigger']")
	POST_CODE = (By.XPATH, "//input[@id='billingAddressAddressZipcode']")
	CITY = (By.CSS_SELECTOR, "//div[@class='e-custom-select__trigger']")
	COUNTRY = (By.CSS_SELECTOR, "//div[@class='custom-select e-custom-select']")
	TOWN = (By.CSS_SELECTOR, "//div[@class='custom-select e-custom-select']")
	PHONE_NUMBER = (By.XPATH, "//input[@id='billingAddressAddressPhoneNumber']")

	NEXT_BUTTON = (By.XPATH, "//button[@class='btn btn-primary btn-lg']")

	def navigate_to_homepage(self):
		self.chrome.get("https://www.douglas.ro/account/login")

	ACCEPT_BUTTON = (By.XPATH, '//button[@data-testid="uc-accept-all-button]')
	def accept_cookies(self):
		try:
			shadow_element = Shadow(self.chrome)
			shadow_element.get_shadow_element(*self.ACCEPT_BUTTON)
		except:
			pass

	def client_type(self):
		client_type = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.CLIENT_TYPE))
		client_type.send_keys(client_type)

	def client_gen(self):
		client_gen = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.CLIENT_GEN))
		client_gen.send_keys(client_gen)

	def insert_firstname(self, firstname="Ioana"):
		firstname = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.FIRSTNAME))
		firstname.send_keys(firstname)

	def insert_name(self, insert_name = "Popescu"):
		name = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.NAME))
		name.send_keys(name)

	def email(self, email="ioana.popescu@yahoo.com"):
		email = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.EMAIL))
		email.send_keys(email)

	def password(self, password="12345678"):
		password = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.PASSWORD))
		password.send_keys(password)

	def street_and_number(self, street_and_number="12"):
		street_and_number = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.STREET_AND_NUMBER))
		street_and_number.send_keys(street_and_number)

	def block(self, block="10"):
		block = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.BLOCK))
		block.send_keys(block)

	def scale(self, scale="4A"):
		scale = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.SCALE))
		scale.send_keys(scale)

	def floor(self, floor="1"):
		floor = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.FLOOR))
		floor.send_keys(floor)

	def house_number(self, house_number="3"):
		house_number = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.HOUSE_NUMBER))
		house_number.send_keys(house_number)

	def sector(self, sector="4"):
		sector = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.SECTOR))
		sector.send_keys(sector)

	def post_code(self, post_code="600089"):
		post_code = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.POST_CODE))
		post_code.send_keys(post_code)

	def city(self, city="Bucuresti"):
		city = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.CITY))
		city.send_keys(city)

	def country(self, country="Romania"):
		country = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.COUNTRY))
		country.send_keys(country)

	def town(self, town="Romania"):
		town = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.TOWN))
		town.send_keys(town)

	def phone_number(self, phone_number="0744123456"):
		phone_number = WebDriverWait(self.chrome, 3).until(EC.presence_of_element_located(self.PHONE_NUMBER))
		phone_number.send_keys(phone_number)

	def click_next_button(self):
		self.chrome.find_element(*self.NEXT_BUTTON).click()

	def check_current_url(self):
		actual_url = self.chrome.current_url
		expected_url = 'https://www.douglas.ro/account'
