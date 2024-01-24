from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Base_page


class Home_page(Base_page):

	def accept_cookies(self):
		try:
			shadow_element = Shadow(self.chrome)
			shadow_element.get_shadow_element(*self.ACCEPT_BUTTON)
		except:
			pass
		ACCOUNT_DROPDOWN = (By.CSS_SELECTOR, "//div[@class='account-menu-login']")
		LOGOUT_LINK = (By.LINK_TEXT, 'Logout')

		def logout_of_the_application(self):
			account_dropdown = WebDriverWait(self.chrome, 10).until(
				EC.presence_of_element_located(self.ACCOUNT_DROPDOWN))
			account_dropdown.click()
			self.chrome.find_element(*self.LOGOUT_LINK).click()
