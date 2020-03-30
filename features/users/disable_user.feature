@disable_user @all @user
Feature: Disable User

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
     Then user type "client" in autocomplete textbox role
     Then user will click send invite
     Then user will logout

  Scenario: User can disable account
    Given a user will logged in
     Then user will navigates to Users page
     When user in "Users" page
     Then user will find "gbf.rhtest@gmail.com" in Users page
     Then user will click disable button
     Then user will logout