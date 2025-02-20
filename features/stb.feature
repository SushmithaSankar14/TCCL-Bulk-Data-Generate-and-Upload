Feature: Create Customer in SMS

  @CreateSTB
  Scenario: Create Customer in successfully
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click STB Module
    Then add New Stb

  @CheckAllStbMenu @stage
  Scenario: Check All Stb SubMenu
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click STB Module
    Then Verify STB BredCrumb
    Then Verify Stb BulkOperations
    Then Verify Stb VCPairing
