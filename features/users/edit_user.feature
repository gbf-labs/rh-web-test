@update_user @all @user
Feature: Update User Account

  Scenario: User can send an invite
    Given a user will logged in
     Then user will navigates to Users page
     When user in "Users" page
     Then user will click invite button
     When user in "invite user" page
     Then user type "Test" in first name
     Then user type "nothing" in middle name
     Then user type "GBF" in last name
     Then user type "gbf.rhtest@gmail.com" in email address
     Then user type "Radio Holland BE" in autocomplete textbox company
     Then user "enable" allow VPN access if vessel "LaboBE01" exists
     Then user type "dummy" in autocomplete textbox role
     Then user will click send invite
     Then user will logout

  Scenario: User can update an account
    Given a user will logged in
     Then user will navigates to Users page
     When user in "Users" page
     Then user will find "gbf.rhtest@gmail.com" in Users page
     Then user will click edit button
     When user in "update user" page
     Then user type "RH" in first name
     Then user type "nothing" in middle name
     Then user type "GBF" in last name
    #  Then user type "gbf.rhtest@gmail.com" in email address
     Then user type "Radio Holland BE" in autocomplete textbox company
     Then user "enable" allow VPN access if vessel "LaboBE01" exists
     Then user type "dummy" in autocomplete textbox role
     Then user will click update user
     Then user will logout