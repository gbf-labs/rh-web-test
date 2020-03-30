@skip @delete_device_image @device_image
Feature: Delete Device Image

  Scenario: User can delete device image
    Given a user will logged in
     Then user will navigates to Admin Devices page
     When user in "Admin Devices" page
     Then user find "ALP Winger" in Admin Device List
     Then user will look for "NMEA2" device in "ALP Winger" tab and "delete"
     Then user will confirm delete of device image
     Then user will logout