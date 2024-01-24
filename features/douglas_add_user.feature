Feature: Test all the functionalities for adding a user

  Background:
    Given User can create new account

     @T1  @positiveTesting
  Scenario: Check if the user can enter a name and password
    When The user inserts valid information on the username and password fields
    When The user clicks on the next button
    Then The user create his account

        @T2  @negativeTesting
  Scenario: Check if the user can enter a name and password
    When The user inserts invalid name and invalid password
    When The user clicks on the next button
    Then The user receives error message and cannot create his account