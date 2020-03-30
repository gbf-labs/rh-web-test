@delete_alarm_value @all @alarm_values
Feature: Delete Alarm value

  Scenario: User can create new Alarm Value
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will click create button in alarm value page
     When user in "create alarm values" page
     Then user type "Test1 Time Delta" in name input textbox alarm value
     Then user type "LaboBE01" in vessel input textbox "create" alarm value
     Then user type "Corevalues" in device input textbox "create" alarm value
     Then user type "nothing" in device type input textbox "create" alarm value
     Then user type "Clock" in module input textbox "create" alarm value
     Then user type "TimeDelta" in option input textbox "create" alarm value
     Then user type "Raw Value" in value input textbox "create" alarm value
     Then user will save the new alarm value
     Then user will logout

  Scenario: User can delete alarm values
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will find "Test1 Time Delta" in Alarm Values page
     Then user will click delete alarm value button
     Then user will logout