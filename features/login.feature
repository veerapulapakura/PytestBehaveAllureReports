#@smoke
Feature: Login functionality of web tours

  Background:
    Given The user is on the home page


  @smoke
  Scenario: Validation of login functionality.
    When The user entered the valid username and password
    Then The user should land on the login screen


  Scenario: Validation of login functionality using parameterization.
    When The user entered the valid "mercury" and "mercury"
    Then The user should land on the login screen


  @regression
  Scenario Outline: Validation of login functionality using parameterization.
    When The user entered the valid "<username>" and "<password>"
    Then The user should land on the login screen
    Examples:
      |username  | password |
      |mercury  | mercury |
      |mercury  | mercury |


  @bugfix
  Scenario: Validation of login functionality using table data.
    When The user entered the valid the username and password
    |username  | password |
    |mercury  | mercury |
    Then The user should land on the login screen
