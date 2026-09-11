# Created by sabriamanay at 9/10/26
Feature: Test cases for Target Search

  Scenario: User can search for tea
    Given Open main target page
    When Search for tea
    Then Verify search results are shown for tea