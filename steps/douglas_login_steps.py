from behave import *

@given("The user is on the Douglas login page")
def step_impl(context):
		context.login_page.navigate_to_homepage()
		context.login_page.accept_cookies()
@when('The user inserts valid information on the username and password fields')
# @when('The user inserts valid username "username" and valid password "password"')
def step_impl(context):
		context.login_page.insert_username()
		context.login_page.insert_password()
		# context.login_page.insert_username(username)
		# context.login_page.insert_password(password)

@when('The user clicks on the login button')
def step_impl(context):
		context.login_page.click_login_button()

@then('The user is logged into the application')
def step_impl(context):
		# raise NotImplementedError('Then The user is logged into the application')
		context.login_page.check_current_url()

@then('The user receives error message: "{error_message}" and cannot login into the application')
def step_impl(context,error_message):
		context.login_page.check_error_message(error_message)
		# raise NotImplementedError('Then The user receives error message: "Invalid credentials" and cannot login into the application')

@when('The user inserts username "{email_for_tests@yahoo.com}" and password "{12345678}"')
def step_impl(context,username,password):
		try:
				context.home_page.logout_of_the_application()
		except:
				pass
		context.login_page.insert_username(username)
		context.login_page.insert_password(password)

@given("The user is logged into the application")
def step_impl(context):
		context.login_page.insert_username()
		context.login_page.insert_password()