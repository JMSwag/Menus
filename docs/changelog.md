#Changelog

## v0.2.1 - Master
####* This version is not yet released and is under active development.


## v0.2.0 - 2016/08/08

###Added

  - Py3 compat
  - Ability to provide custom menu name
  - dsdev-utils
  - A few tests
  - pause method on BaseMenu
    - pause(seconds=5, enter_to_continue=False)
  - init BaseMenu(commands=commands)

###Updated

  - Subclass enforcement
  - Re-factored internal api
  - BaseMenu initialization logic
  - Checking of sub-menus

###Fixed

  - Logger naming

###Removed

  - Requirement to pass MainMenu option
  - Duplicate code

###Deprecation

  - Initialize BaseMenu with options -> commands
  - BaseMenu get_correct_action -> get_correct_answer

##v0.1.0 - 2015/07/25

###Initial Commit