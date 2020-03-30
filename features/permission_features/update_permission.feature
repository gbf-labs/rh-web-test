@update_permission @all @permission
Feature: Update permission

  Scenario: User can create new permission
    Given a user will logged in
     Then user will navigates to Permission page
     When user in "Permission" page
     Then user will click create permission button
     When user in "create permission" page
     Then user type "Permission 3" in name input textbox
     Then user type "test 3" in details input textbox
     Then user will save the new permission
     Then user will logout

  Scenario: User can update permission
    Given a user will logged in
     Then user will navigates to Permission page
     When user in "Permission" page
     Then user will find "Permission 3"
     Then user will click edit permission button
     When user in "edit permission" page
     Then user type "[Updated] Permission 3" in name input textbox
     Then user type "test updated 3" in details input textbox
     Then user will update the permission
     Then user will logout