@create_alarm_value @all @alarm_values
Feature: Create Alarm Value

  Scenario: User can create new Alarm Value
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will click create button in alarm value page
     When user in "create alarm values" page
     Then user type "Test Time Delta" in name input textbox alarm value
     Then user type "LaboBE01" in vessel input textbox "create" alarm value
     Then user type "Corevalues" in device input textbox "create" alarm value
     Then user type "nothing" in device type input textbox "create" alarm value
     Then user type "Clock" in module input textbox "create" alarm value
     Then user type "TimeDelta" in option input textbox "create" alarm value
     Then user type "Raw Value" in value input textbox "create" alarm value
     Then user will save the new alarm value
     Then user will logout