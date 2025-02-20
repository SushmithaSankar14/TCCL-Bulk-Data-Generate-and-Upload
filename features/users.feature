Feature: Create Users Functionality For Tccl SMS User Login

  @UsersListPDF
  Scenario: Verify SuperAdmin logs in successfully
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click Users Module
    Then Click download Users list PDF icon
        #Then Click download Users list CSV icon

  @UsersMenu
  Scenario: Check All Users SubMenu
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click Users Module
