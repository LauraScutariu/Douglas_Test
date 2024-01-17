Feature: Check the functionality of the shopping cart

  Background:
    Given Navigate to items page

  @Shopping
  Scenario: Adding one item to the shopping cart
    When We add one item to shopping cart
    Then Count of items in shopping cart is one

   @Shopping
  Scenario: Adding multiple items to the shopping cart
    When We add multiple items to shopping cart
    Then There are multiple items in shopping cart

     @Shopping
  Scenario: I want to remove an item from the shopping cart
    When We add multiple items to shopping cart
    When We regarding an item , we navigate to shopping page
    Then We remove one item from the shopping cart   