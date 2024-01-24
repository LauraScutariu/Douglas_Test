from browser import Browser

from pages.home_page import Home_page
from pages.login_page import Login_page

def before_all(context):
		context.browser = Browser()
		context.login_page = Login_page()
		context.home_page = Home_page()
		# context.add_user_page = Add_user_page()
		context.browser.maximise_window()

def after_all(context):
		context.browser.close_browser()