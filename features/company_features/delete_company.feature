@delete_company @all @demo @company
Feature: Delete company

  Scenario: User can create new company
    Given a user will logged in
     Then user will navigates to company page
     When user in "company" page
     Then user will click create company button
     When user in "create company" page
     Then user type "Company 2" in name input textbox company
     Then user type "LaboBE01" in vessels autocomplete textbox company
     Then user will save the new company
     Then user will logout

  Scenario: User can delete company
    Given a user will logged in
     Then user will navigates to Company page
     When user in "Company" page
     Then user will find "Company 2" in Company page
     Then user will click delete company button
     Then user will logout