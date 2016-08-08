# --------------------------------------------------------------------------
# Copyright (c) 2016 Digital Sapphire
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the
# following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
# ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
# --------------------------------------------------------------------------
import logging
import os
import time

from dsdev_utils.terminal import (ask_yes_no,
                                  get_correct_answer,
                                  get_terminal_size)
import six

from menus.exceptions import MenusError
from menus.utils import clear_screen_cmd, Getch

log = logging.getLogger(__name__)


class BaseMenu(object):

    def __init__(self, **kwargs):
        self.app_name = None
        menu_name = kwargs.get('menu_name')
        if menu_name is None:
            self.menu_name = self.__class__.__name__
        else:
            self.menu_name = menu_name

        self.options = kwargs.get('options')
        if self.options is None:
            self.options = []
        self.message = kwargs.get('message')

    def __call__(self):
        x = self.display()
        x()

    def done(self):
        pass

    def pause(self, seconds=5, enter_to_continue=False):
        if not isinstance(enter_to_continue, bool):
            raise MenusError('enter_to_continue must be boolean',
                             expected=True)
        if not isinstance(seconds, six.integer_types):
            raise MenusError('seconds must be integer', expected=True)

        if enter_to_continue is True:
            six.moves.input('Press enter to quit')
        else:
            time.sleep(seconds)

    def ask_yes_no(self, question, default):
        return ask_yes_no(question, default)

    # ToDo: Remove in v1.0
    def get_correct_action(self, question, default, required):
        return get_correct_answer(question, default, required)
    # End ToDo

    def get_correct_answer(self, question, default, required):
        return get_correct_answer(question, default, required)

    def display(self):
        self._display_menu_header()
        self.display_msg(self.message)
        return self._menu_options(self.options)

    # Takes a string and adds it to the menu header along side
    # the app name.
    def _display_menu_header(self):
        window_size = get_terminal_size()[0]

        def add_style():
            top = '*' * window_size + '\n'
            bottom = '\n' + '*' * window_size + '\n'

            header = self.app_name + ' - ' + self.menu_name
            header = header.center(window_size)
            msg = top + header + bottom
            return msg
        os.system(clear_screen_cmd)
        print(add_style())

    def display_msg(self, message=None):
        window_size = get_terminal_size()[0]
        if message is None:
            return ''

        if not isinstance(message, six.string_types):
            log.warning('Did not pass str')
            return ''

        def format_msg():
            formatted = []
            finished = ['\n']
            count = 0
            words = message.split(' ')
            for w in words:
                w = w + ' '
                if count + len(w) > window_size / 2:
                    finished.append(''.join(formatted).center(window_size))
                    finished.append('\n')
                    count = len(w)
                    # Starting a new line.
                    formatted = []
                    formatted.append(w)
                else:
                    formatted.append(w)
                    count += len(w)
            finished.append(''.join(formatted).center(window_size))
            finished.append('\n')
            return ''.join(finished)
        print(format_msg())

    # Takes a list of tuples(menu_name, call_back) adds menu numbers
    # then prints menu to screen.
    # Gets input from user, then returns the callback
    def _menu_options(self, options=None):
        if options is None:
            return ""
        if not isinstance(options, list):
            return ""

        def add_options():
            getch = Getch()
            menu = []
            count = 1
            for s in options:
                item = '{}. {}\n'.format(count, s[0])
                menu.append(item)
                count += 1
            print(''.join(menu))
            answers = []
            for a in six.moves.range(1, len(menu) + 1):
                answers.append(str(a))
            while 1:
                ans = getch()
                if ans in answers:
                    break
                else:
                    log.debug('Not an acceptable answer!')
            return options[int(ans) - 1][1]
        return add_options()


class MainMenu(BaseMenu):

    def __init__(self, options):
        super(MainMenu, self).__init__(options=options)
