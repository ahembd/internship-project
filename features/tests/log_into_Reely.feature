# Created by alberthembd at 3/12/24
Feature: The user is able to log into the Reely application
  using the Google Developer tools emulator for devices.

  Scenario: The user can log into Really when his client is Google Tools emulator
    set to the size of Samsung Galaxy S20 Ultra
    Given that the user has logged into https://soft.reelly.io/off-plan
    When the user sets emulator size Samsung Galaxy S20 Ultra
    Then user is still able to log in

 # Enter feature name here
  # Enter feature description
  # Scenario: # Enter scenario name here
    # Enter steps here