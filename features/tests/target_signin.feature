# Created by sabriamanay at 9/10/26
Feature: Sign In tests

  Scenario: User  can navigate to Sign In
    Given Open main target page
    When Click Account
    And Click Sign In from right side navigation menu
    Then Verify Sign In form opened