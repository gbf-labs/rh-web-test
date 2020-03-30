@add_user @all @user
Feature: Invite User

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

  Scenario: User can check the email
    Given a user will login to gmail
      Then user will check the "Invitation" email and login to RH site
      When user in "Maps" page
      Then user will logout