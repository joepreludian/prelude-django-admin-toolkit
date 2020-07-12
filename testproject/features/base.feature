Feature: Logged in page

    Scenario: Access index page

        When I access the admin home page
        Then I see the project name on title
        Then I see the fields of login and password

        Given an authenticated user
        When I access the admin home page
        Then I see my username printed
