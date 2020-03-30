@delete_alarm_condition @all @alarm_conditions
Feature: Delete Alarm condition

  Scenario: User can create new Alarm Value
    Given a user will logged in
     Then user will navigates to Alarm Values page
     When user in "Alarm Values" page
     Then user will click create button in alarm value page
     When user in "create alarm values" page
     Then user type "Del1Alarm" in name input textbox alarm value
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
     Then user type "Del2Alarm" in name input textbox alarm value
     Then user type "LaboBE02" in vessel input textbox "create" alarm value
     Then user type "MODEM2" in device input textbox "create" alarm value
     Then user type "Evolution_X5" in device type input textbox "create" alarm value
     Then user type "nothing" in module input textbox "create" alarm value
     Then user type "Tx_State" in option input textbox "create" alarm value
     Then user type "Raw Value" in value input textbox "create" alarm value
     Then user will save the new alarm value
     Then user will logout

  Scenario: User can create new Alarm Condition  
    Given a user will logged in
     Then user will navigates to Alarm Conditions page
     When user in "Alarm Conditions" page
     Then user will click create button in alarm condition page
     When user in "create alarm conditions" page
     Then user type "Alarm Condition Delete" in comment input textbox
     Then user select "True if Param1 > Param2" in "create" Operator
     Then user select "Del1Alarm" in parameter 1
     Then user select "Del2Alarm" in parameter 2
     Then user will save the new alarm condition
     Then user will logout

  Scenario: User can delete alarm conditions
    Given a user will logged in
     Then user will navigates to Alarm Conditions page
     When user in "Alarm Conditions" page
     Then user will find "Alarm Condition Delete" in Alarm Conditions page
     Then user will click delete alarm condition button
     Then user will logout




