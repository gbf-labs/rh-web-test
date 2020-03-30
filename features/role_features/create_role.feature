@create_role @all @role
Feature: Create role

  Scenario: User can create new permission
    Given a user will logged in
     Then user will navigates to Permission page
     When user in "Permission" page
     Then user will click create permission button
     When user in "create permission" page
     Then user type "maps" in name input textbox
     Then user type "maps" in details input textbox
     Then user will save the new permission
     Then user will logout

  Scenario: User can create new role
    Given a user will logged in
     Then user will navigates to role page
     When user in "Role" page
     Then user will click create role button
     When user in "create role" page
     Then user type "dummy" in name input textbox role
     Then user type "Can view maps only" in details input textbox role
     Then user will select "maps" in "create" permissions selection role
     Then user will save the new role
     Then user will logout