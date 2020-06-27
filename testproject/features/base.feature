Feature: Logged in page

    Scenario: Access index page

        Given an authenticated user
        When I access the admin home page
        Then I see my username printed
