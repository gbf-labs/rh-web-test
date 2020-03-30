@update_role @all @role
Feature: Update role

  Scenario: User can create new permission
    Given a user will logged in
     Then user will navigates to Permission page
     When user in "Permission" page
     Then user will click create permission button
     When user in "create permission" page
     Then user type "Permission 103" in name input textbox
     Then user type "test 1" in details input textbox
     Then user will save the new permission
     Then user will logout

  Scenario: User can create new role
    Given a user will logged in
     Then user will navigates to role page
     When user in "Role" page
     Then user will click create role button
     When user in "create role" page
     Then user type "Role 3" in name input textbox role
     Then user type "test 2" in details input textbox role
     Then user will select "Permission 103" in "create" permissions selection role
     Then user will save the new role
     Then user will logout

  Scenario: User can update new role
    Given a user will logged in
     Then user will navigates to role page
     When user in "Role" page
     Then user will find "Role 3"
     Then user will click edit role button
     When user in "edit role" page
     Then user type "Updated role" in name input textbox role
     Then user type "Role for testing" in details input textbox role
     Then user will select "Permission 103" in "update" permissions selection role
     Then user will update the role