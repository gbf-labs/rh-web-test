@create_permission @all @permission
Feature: Create permission

  Scenario: User can create new permission
    Given a user will logged in
     Then user will navigates to Permission page
     When user in "Permission" page
     Then user will click create permission button
     When user in "create permission" page
     Then user type "Permission 1" in name input textbox
     Then user type "test 1" in details input textbox
     Then user will save the new permission
     Then user will logout