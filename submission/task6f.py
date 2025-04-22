Scenario: Search by category
    When I visit the "Home Page"
    And I press the "Clear" button
    And I select "Food" in the "Category" dropdown
    And I press the "Search" button
    Then I should see the message "Success"
    And I should see "Big Mac" in the results
    And I should see "Hat" in the results
    And I should see "Shoes" in the results
    And I should see "Sheets" in the results
