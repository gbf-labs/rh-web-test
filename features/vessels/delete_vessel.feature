@delete_vessel @all @vessels
Feature: Delete Vessel

  Scenario: User can create vessel
    Given a user will logged in
     Then user will navigates to Vessel page
     When user in "Vessel" page
     Then user will click create vessel button
     When user in "create vessel" page
     Then user type "VTest" in vessel name input textbox
     Then user type "2040" in vessel imo input textbox
     Then user will save the new vessel
     Then user will logout

  Scenario: User can delete vessel
    Given a user will logged in
     Then user will navigates to Vessel page
     When user in "Vessel" page
     Then user will find "VTest" in Vessel page
     Then user will click delete vessel button
     Then user will logout