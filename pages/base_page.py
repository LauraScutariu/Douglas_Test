from pyshadow.main import Shadow
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser

class Base_page(Browser):
	ACCEPT_BUTTON = (By.XPATH, '//button[@data-testid="uc-accept-all-button]')
	def accept_cookies(self):
		try:
			shadow_element = Shadow(self.chrome)
			shadow_element.get_shadow_element(*self.ACCEPT_BUTTON)
		except:
			pass

		def check_error_message(self, by, selector, expected_error_message):
				error_message_web_element = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located((by,selector)))
				actual_error_message_text = error_message_web_element.text

				assert expected_error_message == actual_error_message_text, f"Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}"