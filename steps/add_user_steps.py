from behave import *

@given('User can create new account')
def step_impl(context):
		context.home_page.navigate_to_homepage()
		context.home_page.accept_cookies()
@when('The user inserts valid information on the username and password fields')
def step_impl(context):
		context.home_page.insert_name()
		context.home_page.insert_password()

@when('The user clicks on the next button')
def step_impl(context):
		context.home_page.click_next_button()

@then('The user create his account')
def step_impl(context):
		context.home_page.check_current_url()

@when('The user inserts invalid name and invalid password')
def step_impl(context,name,password):
		context.home_page.insert_name(name)
		context.home_page.insert_password(password)

# @when('The user clicks on the next button')
# def step_impl(context):
# 		context.home_page.click_next_button()

@then('The user receives error message and cannot create his account')
def step_impl(context):
		context.home_page.check_current_url()