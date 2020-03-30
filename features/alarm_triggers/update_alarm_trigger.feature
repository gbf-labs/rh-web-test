@update_alarm_trigger @all @alarm_triggers
Feature: Update Alarm Trigger

  Scenario: User can create new Alarm Trigger
    Given a user will logged in
     Then user will navigates to Alarm Triggers page
     When user in "Alarm Triggers" page
     Then user will click create button in Alarm Trigger page 
     When user in "create alarm triggers" page
     Then user type "Test2" in label input textbox alarm trigger
     Then user type "For Testing" in description input textbox alarm trigger
     Then user "disable" the alarm enable toggle alarm trigger
     Then user "enable" the alarm acknowledge toggle alarm trigger
     Then user select "Critical" in "create" Alarm Types
     Then user select "Test" in "create" Alarm Conditions
     Then user will save the new alarm trigger
     Then user will logout

  Scenario: User can update Alarm Trigger
    Given a user will logged in
     Then user will navigates to Alarm Triggers page
     When user in "Alarm Triggers" page
     Then user will find "Test2" in Alarm Triggers page
     Then user will click update button in alarm trigger page
     When user in "update alarm triggers" page
     Then user type "Test Update" in label input textbox alarm trigger
     Then user type "For Testing Update" in description input textbox alarm trigger
     Then user "disable" the alarm enable toggle alarm trigger
     Then user "enable" the alarm acknowledge toggle alarm trigger
     Then user select "Warning" in "update" Alarm Types
     Then user select "Test" in "update" Alarm Conditions
     Then user will update the alarm trigger
     Then user will logout