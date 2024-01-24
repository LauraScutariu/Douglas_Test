from behave import *


@given('The user navigate to main page')
def step_impl(context):
	context.items_page.navigate_to_item()


@when('User logs into account with email and password')
def step_impl(context):
	context.items_page.login_into_account()


@when('He search for a desire item')
def step_impl(context):
	context.items_page.search_items()


@when('He add the item to the shopping cart')
def step_impl(context):
	context.items_page.add_item()


@when('He proceeds to checkout')
def step_impl(context):
	context.items_page.checkout()


@when('He places the order')
def step_impl(context):
	context.items_page.place_the_order()


@then('The order is placed,succes message "Your order number is:"')
def step_impl(context):
	context.items_page.order_placed_with_succes()