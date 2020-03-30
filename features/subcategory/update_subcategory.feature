@update_subcategory @all @subcategory
Feature: Delete subcategory

  Scenario: User can create new subcategory
    Given a user will logged in
     Then user will navigates to Sub Category page
     When user in "Sub Category" page
     Then user will click create subcategory button
     When user in "create sub category" page
     Then user type "UpAdmin" in subcategory name input textbox
     Then user select "SerialNumber" in "create" options selection
     Then user will save the new subcategory
     Then user will logout

  Scenario: User can update new subcategory
    Given a user will logged in
     Then user will navigates to Sub Category page
     When user in "Sub Category" page
     Then user will find "UpAdmin" in Sub Category page
     Then user will click edit subcategory button
     When user in "update sub category" page
     Then user type "UpdatedSubcat" in subcategory name input textbox
     Then user select "ImoNumber" in "update" options selection
     Then user will update the subcategory
     Then user will logout