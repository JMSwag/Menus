# Menus
Create cli menus with ease


### Installation

```
$ pip install menus
```


### Usage

```python
from menus import BaseMenu, Engine


# Create menu. Class title will be used in header
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

menus = [Cool(), Hot()]

engine = Engine(app_name='My App', menus=menus)

engine.start()
```