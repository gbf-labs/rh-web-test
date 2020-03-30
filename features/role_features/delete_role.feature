@delete_role @all @role
Feature: Delete role

  Scenario: User can create new permission
    Given a user will logged in
     Then user will navigates to Permission page
     When user in "Permission" page
     Then user will click create permission button
     When user in "create permission" page
     Then user type "Permission 102" in name input textbox
     Then user type "test 1" in details input textbox
     Then user will save the new permission
     Then user will logout

  Scenario: User can create new role
    Given a user will logged in
     Then user will navigates to role page
     When user in "Role" page
     Then user will click create role button
     When user in "create role" page
     Then user type "Role 2" in name input textbox role
     Then user type "test 2" in details input textbox role
     Then user will select "Permission 102" in "create" permissions selection role
     Then user will save the new role
     Then user will logout

  Scenario: User can delete role
    Given a user will logged in
     Then user will navigates to Role page
     When user in "Role" page
     Then user will find "Role 2" in Role page
     Then user will click delete role button
     Then user will logout