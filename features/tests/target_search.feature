# Created by sabriamanay at 9/10/26
Feature: Test cases for Target Search

  Scenario: User can search for tea
    Given Open main target page
    When Search for tea
    Then Verify search results are shown for tea


  Scenario Outline: User can search for a product
    Given Open main target page
    When Search for <product>
    Then Verify search results are shown for <expected_product>
    Examples:
    |product  |expected_product |
    |coffee   |coffee           |
    |tea      |tea              |