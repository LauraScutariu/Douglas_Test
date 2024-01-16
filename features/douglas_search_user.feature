Feature: test all the scenarios related to searching a user into the application

  Background:
    Given The user is logged into the application

  Scenario:
    When User clicks on Admin option in the left side menu
    When User selects status "Disabled" in the Search User section
    When User clicks Search button
    Then The users that have the corresponding status are returned