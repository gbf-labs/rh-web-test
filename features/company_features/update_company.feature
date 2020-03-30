@update_company @all @demo @company
Feature: Update company

  Scenario: User can create new company
    Given a user will logged in
     Then user will navigates to company page
     When user in "company" page
     Then user will click create company button
     When user in "create company" page
     Then user type "Company 3" in name input textbox company
     Then user type "LaboBE01" in vessels autocomplete textbox company
     Then user will save the new company
     Then user will logout

  Scenario: User can update new company
    Given a user will logged in
     Then user will navigates to company page
     When user in "company" page
     Then user will find "Company 3"
     Then user will click edit company button
     When user in "edit company" page
     Then user type "Update [Company 3]" in name input textbox company
     Then user type "LaboBE02" in vessels autocomplete textbox company
     Then user will update the company
     Then user will logout