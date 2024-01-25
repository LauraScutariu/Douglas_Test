from pyshadow.main import Shadow
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.core import driver

from pages.base_page import Base_page


class Home_page(Base_page):
    ACCEPT_BUTTON = (By.XPATH, '//button[@data-testid="uc-accept-all-button]')
    LOGIN_LINK = "https://www.douglas.ro/account"
    LOGIN_TO_THE_APPLICATION = "https://www.douglas.ro/account"
    SEARCH_BOX = (By.NAME, "//input[@type='search']")
    ADD_IN_SHOPPING_CART = (By.XPATH, "//input[@id='personalFirstName']")

def accept_cookies(self):
        try:
            shadow_element = Shadow(self.chrome)
            shadow_element.get_shadow_element(*self.ACCEPT_BUTTON)
        except:
            pass

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