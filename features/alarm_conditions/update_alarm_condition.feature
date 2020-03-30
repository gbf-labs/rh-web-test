@update_alarm_condition @all @alarm_conditions
Feature: Update Alarm Condition

  Scenario: User can create new Alarm Value
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will click create button in alarm value page
     When user in "create alarm values" page
     Then user type "Alarm Value1" in name input textbox alarm value
     Then user type "LaboBE02" in vessel input textbox "create" alarm value
     Then user type "VSAT1" in device input textbox "create" alarm value
     Then user type "Intellian_V100_E2S" in device type input textbox "create" alarm value
     Then user type "nothing" in module input textbox "create" alarm value
     Then user type "TxMode" in option input textbox "create" alarm value
     Then user type "Raw Value" in value input textbox "create" alarm value
     Then user will save the new alarm value
     Then user will logout
     
  Scenario: User can create new Alarm Value
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will click create button in alarm value page
     When user in "create alarm values" page
     Then user type "Alarm Value2" in name input textbox alarm value
     Then user type "LaboBE02" in vessel input textbox "create" alarm value
     Then user type "VSAT1" in device input textbox "create" alarm value
     Then user type "Intellian_V100_E2S" in device type input textbox "create" alarm value
     Then user type "nothing" in module input textbox "create" alarm value
     Then user type "TxMode" in option input textbox "create" alarm value
     Then user type "Raw Value" in value input textbox "create" alarm value
     Then user will save the new alarm value
     Then user will logout

  Scenario: User can create new Alarm Condition  
    Given a user will logged in
     Then user will navigates to Alarm Conditions page
     When user in "Alarm Conditions" page
     Then user will click create button in alarm condition page
     When user in "create alarm conditions" page
     Then user type "Alarm Condition Update" in comment input textbox
     Then user select "True if Param1 > Param2" in "create" Operator
     Then user select "Alarm Value1" in parameter 1
     Then user select "Alarm Value2" in parameter 2
     Then user will save the new alarm condition
     Then user will logout

  Scenario: User can update Alarm Condition
    Given a user will logged in
     Then user will navigates to Alarm Conditions page
     When user in "Alarm Conditions" page
     Then user will find "Alarm Condition Update" in Alarm Conditions page
     Then user will click update button in alarm condition page
     When user in "update alarm conditions" page
     Then user type "Updated [Alarm Condition]" in comment input textbox
     Then user select "True if Param1 > Param2" in "update" Operator
     Then user select "Alarm Value1" in parameter 1
     Then user select "Alarm Value2" in parameter 2
     Then user will update the alarm condition
     Then user will logout