Feature: Login Functionality For Tccl sms User Login

  @TCCL_SMS
  Scenario: Verify User logs in successfully
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
