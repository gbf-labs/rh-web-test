@create_company @all @demo @company
Feature: Create Company

  Scenario: User can create new company
    Given a user will logged in
     Then user will navigates to company page
     When user in "company" page
     Then user will click create company button
     When user in "create company" page
     Then user type "Company 1" in name input textbox company
     Then user type "LaboBE01" in vessels autocomplete textbox company
     Then user will save the new company
     Then user will logout