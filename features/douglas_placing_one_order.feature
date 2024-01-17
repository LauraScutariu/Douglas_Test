Feature: Verify placing an order works.

  Background: The user navigate to main page

 @Order
 Scenario: Log in and placing an order
   When User logs into account with email and password
   When He search for a desire item
   When He add the item to the shopping cart
   When He proceeds to checkout
   When He places the order
   Then The order is placed,succes message "Your order number is:"