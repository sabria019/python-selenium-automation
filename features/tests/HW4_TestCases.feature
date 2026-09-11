# Created by sabriamanay at 9/10/26
Feature: HW4 Target Test Cases

  Scenario: User can verify storycards
    Given Open Target Circle page
    Then Verify there are 2 storycards under Unlock added value

  Scenario: User can add a product to cart
    Given Open main target page
    When Search for mug
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)

# Homework 4 Submission