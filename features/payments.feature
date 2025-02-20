Feature: Payments Functionality

  @TCCLPayments @stage
  Scenario: Verify the wallet ledger amount for deposit users
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After Click Payments Module
