from behave import *


@given('Navigate to items page')
def step_impl(context):
	context.items_page.navigate_to_item()


@when('We add one item to shopping cart')
def step_impl(context):
	context.items_page.add_one_item()


@then('Count of items in shopping cart is one')
def step_impl(context):
	context.items_page.check_one_item_in_cart()
	context.shopping_cart_page.navigate_to_shopping_cart()
	context.shopping_cart_page.clear_all_items()


@when('We add multiple items to shopping cart')
def step_impl(context):
	context.items_page.add_multiple_items()


@then('There are multiple items in shopping cart')
def step_impl(context):
	context.items_page.check_multiple_items_in_cart()
	context.shopping_cart_page.navigate_to_shopping_cart()
	context.shopping_cart_page.clear_all_items()


@when('We regarding an item , we navigate to shopping page')
def step_impl(context):
	context.items_page.add_new_item()


@then('We remove one item from the shopping cart')
def step_impl(context):
	context.items_page.check_multiple_items_in_cart()
	context.shopping_cart_page.navigate_to_shopping_cart()
	context.shopping_cart_page.clear_one_item()