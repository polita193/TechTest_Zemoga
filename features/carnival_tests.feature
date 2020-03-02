Feature: Carnival Tests
  # Validate some functionalities of the website www.carnival.com

  Background: Access to Carnival page
    Given a web browser is in Carnival page

  Scenario: Search for a cruise
    When I search a cruise to "The Bahamas" with a duration of "6 - 9 Days"
    Then the results grid is displayed
    And the filter by price option is controlled by an slider
    #And there is an option to sort by price

  Scenario: Review Sail itinerary
    And the results of a cruise search to "The Bahamas" with "6 - 9 Days" duration are shown
    When I select a sail from the results
    Then the book now button is displayed
    And the itinerary by day is displayed