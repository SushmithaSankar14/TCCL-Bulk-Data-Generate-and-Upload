Feature: Create Customer in SMS

  @CreateCustomer
  Scenario: Create Customer in successfully
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click Customer Module
    Then Add New Customer
    Given User Details
