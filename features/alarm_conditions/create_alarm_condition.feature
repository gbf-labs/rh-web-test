@create_alarm_condition @all @alarm_conditions
Feature: Create Alarm Condition

  Scenario: User can create new Alarm Value
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will click create button in alarm value page
     When user in "create alarm values" page
     Then user type "VSAT1 TxMode" in name input textbox alarm value
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
     Then user type "Modem2 TxState" in name input textbox alarm value
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
     Then user type "Test" in comment input textbox
     Then user select "True if Param1 > Param2" in "create" Operator
     Then user select "VSAT1 TxMode" in parameter 1
     Then user select "Modem2 TxState" in parameter 2
     Then user will save the new alarm condition
     Then user will logout