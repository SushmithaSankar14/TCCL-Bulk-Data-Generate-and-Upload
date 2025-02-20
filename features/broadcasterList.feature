Feature: Verify broadcaster List feature in Channels Module

  @ChannelsBroadcasterList
  Scenario: Verify creation of broadcaster
    Given Launch browser
    When the user navigates to TCCL SMS login page
    Then Enter userName and password
    Then Click continue button for SMS User Login
    Then move to channels
    And move to broadcasterList in channels module
    And click create broadcaster button
    And enter all the fields with valid data
    Then click create button when enabled for broadcaster creation
