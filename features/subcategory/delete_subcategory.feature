@delete_subcategory @all @subcategory
Feature: Delete subcategory

  Scenario: User can create new subcategory
    Given a user will logged in
     Then user will navigates to Sub Category page
     When user in "Sub Category" page
     Then user will click create subcategory button
     When user in "create sub category" page
     Then user type "SubDelete" in subcategory name input textbox
     Then user select "SerialNumber" in "create" options selection
     Then user will save the new subcategory
     Then user will logout



  Scenario: User can delete subcategory
    Given a user will logged in
     Then user will navigates to Sub Category page
     When user in "Sub Category" page
     Then user will find "SubDelete" in Sub Category page
     Then user will click delete subcategory button
     Then user will logout