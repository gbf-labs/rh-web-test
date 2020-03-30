@create_vessel @all @vessels
Feature: Create Vessel

  Scenario: User can create vessel
    Given a user will logged in
     Then user will navigates to Vessel page
     When user in "Vessel" page
     Then user will click create vessel button
     When user in "create vessel" page
     Then user type "Vessel Test" in vessel name input textbox
     Then user type "IMO Test" in vessel imo input textbox
     Then user will save the new vessel
     Then user will logout