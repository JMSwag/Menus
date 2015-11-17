# Menus
Create cli menus with ease


### Installation

```
$ pip install menus
```


### Usage

Fast navigation! Menu advances on number press. No need to hit enter.

######Limitation: Max of 8 options per menu. 64 commands total

```python
from menus import BaseMenu, Engine


# Classes are used to create menus.
# Class title will be used for menu header
class Cool(BaseMenu):

    def __init__(self):
        # An option is a tuple which consists of ('Display Name', function)
        options = [('Speak', self.speak), ('Main Menu', self.done)]
        super(Cool, self).__init__(options=options)

    def speak(self):
        # Used to nicely display a message towards the
        # middle of the screen
        self.display_msg('Cool is speaking')
        input()
        # Used to return to Cool Menu. If omitted
        # You'll be returned to the Main Menu
        self()


class Hot(BaseMenu):

    def __init__(self):
        options = [('Speak', self.speak), ('Main Menu', self.done)]
        super(Hot, self).__init__(options=options)

    def speak(self):
        self.display_msg("It's getting hot in here")
        input()
        self()


class Keys(BaseMenu):

    def __init__(self):
        options = [('Show Public Key', self.show_public_key)]

        super(Keys, self).__init__(options=options)
        # self.menu = Menu(header, options)

    def show_public_key(self):
        log.debug('Show public key')
        self.display_msg('thdkalfjl;da;ksfkda;fdkj')
        self.display_msg('Press enter to quit')
        input()
        self()


engine = Engine(app_name='My App', menus=[Cool(), Hot(), Keys()])

engine.start()
```

### Demo

Use the below example to see Menus in action

```python
from menus import Engine

engine = Engine(example=True)

engine.start()
```

![alt text](https://ds-website-images-all-sites.s3.amazonaws.com/menus-screenshot.png)

### Source
[Github](https://github.com/JMSwag/Menus)

