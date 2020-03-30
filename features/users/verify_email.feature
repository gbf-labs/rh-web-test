  
@verify_user
Feature: Verify Email

  Scenario: User can check the email
    Given a user will login to gmail
      Then user will check the "Re-Invitation" email and login to RH site
      When user in "Maps" page
      Then user will logout