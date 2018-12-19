Feature: Login

    Scenario: Valid login
        Given I go to Login page
        When I type "pawelk9@gmail.com" in email
        And I type "AqZ28ueEsVwi8SD" in password
        And I click log in
        Then I should be logged in

    Scenario: Invalid login
        Given I go to Login page
        When I type "pawelk9@gmail.com" in email
        And I type "qwerty" in password
        And I click log in
        Then Error is displayed
        And I close the browser
