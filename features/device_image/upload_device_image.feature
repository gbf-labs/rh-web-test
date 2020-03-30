@skip @upload_device_image @device_image
Feature: Upload Device Image

  Scenario: User can upload device image
    Given a user will logged in
     Then user will navigates to Admin Devices page
     When user in "Admin Devices" page
     Then user find "ALP Winger" in Admin Device List
    #  When user in "ALP Winger" tab
     Then user will look for "NMEA2" device in "ALP Winger" tab and "upload"
     When user in "Upload Device Image" page
     Then user will choose file to upload
     Then user will click upload
     Then user will logout
  