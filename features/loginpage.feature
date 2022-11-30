Feature: Login orangeHR
  Scenario: Logo presence in login page
    Given :launch chrome browser
    When :open orange HRpage
    Then :verify the logo presence
    And :close browser