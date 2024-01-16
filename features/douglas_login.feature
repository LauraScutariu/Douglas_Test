Feature: Check that the login functionality of the Douglas website is working properly
   Background:
    Given The user is on the Douglas login page

    @T1  @positiveTesting
  Scenario: Check that the user can login into the application when inserting valid username and valid password
    When The user inserts valid information on the username and password fields
#"12345678"
    When The user clicks on the login button
    Then The user is logged into the application

        @T2  @negativeTesting
  Scenario: Check that the user cannot login into the application when inserting invalid username and valid password
    When The user inserts invalid username and valid password
    When The user clicks on the login button
    Then The user receives error message and cannot login into the application

    @T3  @negativeTesting
  Scenario: Check that the user cannot login into the application when inserting invalid username and valid password
    When The user inserts valid username and invalid password
    When The user clicks on the login button
    Then The user receives error message and cannot login into the application


  @T4  @negativeTesting
  Scenario: Check that the user cannot login into the application when inserting invalid username and valid password
    When The user inserts invalid username and invalid password
    When The user clicks on the login button
    Then The user receives error message and cannot login into the application

  @T5 @negativeTesting
  Scenario Outline: Check that the user cannot login into the application when inserting invalid credentials
    When The user inserts username "<username>" and password "<password>"
    When The user clicks on the login button
    Then The user receives error message: "<error_message>" and cannot login into the application
    Examples:
      | username     | password     | error_message       |
      | Admin        | testPassword | Invalid credentials |
      | testUsername | admin123     | Invalid credentials |
      | testUsername | testPassword | Invalid credentials |

  @T6 @negativeTesting
  Scenario Outline: Check that the user cannot login into the application when inserting invalid credentials
    When The user inserts username "<username>" and password "<password>"
    When The user clicks on the login button
    Then The user receives error message: "Invalid credentials" and cannot login into the application
    Examples:
      | username     | password     |  |
      | Admin        | testPassword |  |
      | testUsername | admin123     |  |
      | testUsername | testPassword |  |