#Menus
A CLI UI framework

[![](https://badge.fury.io/py/Menus.svg)](http://badge.fury.io/py/Menus)
[![](https://requires.io/github/JMSwag/Menus/requirements.svg?branch=master)](https://requires.io/github/JMSwag/Menus/requirements/?branch=master)
[![Build Status](https://travis-ci.org/JMSwag/Menus.svg?branch=master)](https://travis-ci.org/JMSwag/Menus)
[![Code Health](https://landscape.io/github/JMSwag/Menus/master/landscape.svg?style=flat)](https://landscape.io/github/JMSwag/Menus/master)
[![Coverage Status](https://coveralls.io/repos/github/JMSwag/Menus/badge.svg)](https://coveralls.io/github/JMSwag/Menus)

![alt text](https://ds-website-images-all-sites.s3.amazonaws.com/menus-screenshot.png)


###Installation

```
$ pip install menus
```


###Usage

```python
from menus import BaseMenu, Engine


# Classes are used to create menus.
# Class title will be used for menu header
class Cool(BaseMenu):

    def __init__(self):
        # An option is a tuple which consists of ('Display Name', function)
        options = [('Speak', self.speak)]
        super(Cool, self).__init__(options=options)

    def speak(self):
        # Used to nicely display a message towards
        # the middle of the screen
        self.display_msg('Cool is speaking')

        # Will pause for 3 seconds
        self.pause()

        # Used to return to Cool Menu. If omitted
        # the user will be returned to the Main Menu
        self()


class Hot(BaseMenu):

    def __init__(self):
        # An option is a tuple which consists of ('Display Name', function)
        options = [('Speak', self.speak)]
        super(Hot, self).__init__(options=options, menu_name='Really Hot')

    def speak(self):
        # Used to nicely display a message towards
        # the middle of the screen
        self.display_msg("It's getting hot in here!")

        # Will pause for 3 seconds
        self.pause(seconds=3)

        # Used to return to Cool Menu. If omitted
        # the user will be returned to the Main Menu
        self()


class Keys(BaseMenu):

    def __init__(self):
    # An option is a tuple which consists of ('Display Name', function)
        options = [('Show Public Key', self.show_public_key)]

        super(Keys, self).__init__(options=options)

    def show_public_key(self):
        log.debug('Show public key')

        # Used to nicely display a message towards
        # the middle of the screen
        self.display_msg('thdkalfjl;da;ksfkda;fdkj')

        # Will prompt user to press enter to continue
        self.pause(enter_to_continue=True)

        # Used to return to Cool Menu. If omitted
        # the user will be returned to the Main Menu
        self()


engine = Engine(app_name='My App', menus=[Cool(), Hot(), Keys()])

engine.start()
```

###Demo

Use the code below to see the Menus demo in action. Note that the menu advances on number press. No need to hit enter.

```python
from menus import Engine

engine = Engine(example=True)

engine.start()
```

###Limitation

8 sub-menus per app. 8 commands per sub-menu. 64 commands total
