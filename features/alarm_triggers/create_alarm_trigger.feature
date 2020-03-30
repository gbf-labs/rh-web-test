@create_alarm_trigger @all @alarm_triggers
Feature: Create Alarm Trigger

  Scenario: User can create new Alarm Trigger
    Given a user will logged in
     Then user will navigates to Alarm Triggers page
     When user in "Alarm Triggers" page
     Then user will click create button in Alarm Trigger page 
     When user in "create alarm triggers" page
     Then user type "Test" in label input textbox alarm trigger
     Then user type "For Testing" in description input textbox alarm trigger
     Then user "disable" the alarm enable toggle alarm trigger
     Then user "enable" the alarm acknowledge toggle alarm trigger
     Then user select "Critical" in "create" Alarm Types
     Then user select "Test" in "create" Alarm Conditions
     Then user will save the new alarm trigger
     Then user will logout