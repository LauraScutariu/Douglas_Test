from pages.home_page import Home_page
from behave import *


home_page = Home_page()

@given('home: I am a user on home page')
def step_impl(context):
	home_page.navigate_to_home_page()

@when('home: I click login button')
def step_impl(context):
	home_page.click_login_button()