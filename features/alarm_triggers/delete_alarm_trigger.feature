@delete_alarm_trigger @all @alarm_triggers
Feature: Delete Alarm Trigger

  Scenario: User can create new Alarm Trigger
    Given a user will logged in
     Then user will navigates to Alarm Triggers page
     When user in "Alarm Triggers" page
     Then user will click create button in Alarm Trigger page 
     When user in "create alarm triggers" page
     Then user type "Test1" in label input textbox alarm trigger
     Then user type "For Testing" in description input textbox alarm trigger
     Then user "disable" the alarm enable toggle alarm trigger
     Then user "enable" the alarm acknowledge toggle alarm trigger
     Then user select "Critical" in "create" Alarm Types
     Then user select "Test" in "create" Alarm Conditions
     Then user will save the new alarm trigger
     Then user will logout

  Scenario: User can delete alarm triggers
    Given a user will logged in
     Then user will navigates to Alarm Triggers page
     When user in "Alarm Triggers" page
     Then user will find "Test1" in Alarm Triggers page
     Then user will click delete alarm trigger button
     Then user will logout