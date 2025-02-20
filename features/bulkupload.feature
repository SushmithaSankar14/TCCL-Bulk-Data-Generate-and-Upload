Feature: Bulk Uplod successfully

  @Bulkupload @stage
  Scenario: Bulk Upload Stb
    When generate Bulkdata
    Then verify the data is generated correctly
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click STB Module
    Then Verify STB BredCrumb
    Then click Create STB
    Then bulk Upload Create STB
    Then after Upload Verify the stb
    # #Then Create STB API Response check
    Then click Transfer STB and upload
    Then Upload bulk Create Subscriber
    Then Upload Bulk data for Product
    Then After upload verify Product
  # Then After login Click STB Module
  # Then Verify Stb BulkOperations
  # And Upload bulk data for STB Deactivation
  # # # And Upload bulk data for STB Activation
  # # # And Upload bulk data for STB Deactivation
  # And Upload bulk data for STB Reactivation
  # Then Upload bulk data for STB deactivation reasons deactivated by MSO
  # Then Upload bulk data for STB Activation reasons Trial pack
    Then Upload Bulk Intro LCO Transfer

  @BulkDataGenerate
  Scenario: generate Bulk data
    When generate Bulkdata
    Then verify the data is generated correctly

  @CreateSTBBulkDataUpload
  Scenario: Bulk data upload in create Stb
    When generate Bulkdata
    Then verify the data is generated correctly
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click STB Module
    Then Verify STB BredCrumb
    Then click Create STB
    Then bulk Upload Create STB

  @afterUploadCreateSTBVerification
  Scenario: STB Verification
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then After login Click STB Module
    Then Verify STB BredCrumb
    Then click Create STB
    Then after Upload Verify the stb
