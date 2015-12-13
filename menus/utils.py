# The MIT License (MIT)
#
# Copyright (c) 2014 JohnyMoSwag <johnymoswag@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
from __future__ import print_function
import logging
import os
import platform
import shlex
import struct
import subprocess
import sys

import six

from menus.exceptions import MenusError

# Preventing import errors on non windows
# platforms
if sys.platform == 'win32':
    import msvcrt
else:
    import termios
    import tty


log = logging.getLogger(__name__)

py3 = sys.version_info.major == 3
py2 = sys.version_info.major == 2
FROZEN = getattr(sys, 'frozen', False)

if sys.platform == 'win32':
    clear = 'cls'
else:
    clear = 'clear'

# We will use input internally to support
# python 2 & 3
if py2:
    range = xrange


class BaseMenu(object):

    def __init__(self, app_name=None, options=None, message=None):
        self.app_name = app_name
        self.options = options
        self.message = message

    def __call__(self):
        x = self.display()
        x()

    def done(self):
        pass

    def ask_yes_no(self, question, default):
        return ask_yes_no(question, default)

    def get_correct_action(self, question, default, required):
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

            header = self.app_name + ' - ' + self.__class__.__name__
            header = header.center(window_size)
            msg = top + header + bottom
            return msg
        os.system(clear)
        print(add_style())

    def display_msg(self, message=None):
        window_size = get_terminal_size()[0]
        if message is None:
            return ''

        if not isinstance(message, str):
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
            getch = _Getch()
            menu = []
            count = 1
            for s in options:
                item = '{}. {}\n'.format(count, s[0])
                menu.append(item)
                count += 1
            print(''.join(menu))
            answers = []
            for a in range(1, len(menu) + 1):
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

    def __init__(self, app_name, options):
        super(MainMenu, self).__init__(app_name, options)


def check_options_else_raise(options):
    # We need a least one thing to display
    # Using this as a teaching aid. Also making the use of
    # Engine(example=Ture) very explicit
    if len(options) == 0:
        msg = ('You must pass a menus object or initilize '
               'like -> Engine(example=True)')
        raise MenusError(msg, expected=True)

    # We need a list or tuple to loop through
    if not isinstance(options, list):
        if not isinstance(options, tuple):
            msg = ('You must pass a list or tuple to menus.')
            raise MenusError(msg, expected=True)

    if len(options) > 9:
        msg = ('Cannot have more then 8 options per menu')
        raise MenusError(msg, expected=True)

    for o in options:
        # Ensuring each item in list/tuple is a tuple
        if not isinstance(o, tuple):
            raise MenusError()

        if len(o) != 2:
            raise MenusError('Invalid number of tuple '
                             'items:\n\n{}'.format(o))
        # Ensure index 0 is a str
        if not isinstance(o[0], six.string_types):
            msg = 'Menus are passed as [("Menu Name", MenuObject())]'
            raise MenusError(msg)


def check_mro(c):
    # Ensure index 1 subclassed BaseMenu
    if issubclass(c.__class__, BaseMenu) is False:
        raise MenusError('Not a sublcass of BaseMenu \n\nclass '
                         '{}'.format(c.__class__.__name__),
                         expected=True)


def ask_yes_no(question, default='no', answer=None):
    """Will ask a question and keeps prompting until
    answered.

    Args:
        question (str): Question to ask end user

    Kwargs:
        default (str): Default answer if user just press enter at prompt

    Returns:
        bool. Meaning::

            True - Answer is  yes

            False - Answer is no
    """
    # Sanitizing user input
    default = default.lower()
    yes = ['yes', 'ye', 'y']
    no = ['no', 'n']
    if default in no:
        default_display = '[N/y]?'
        default = False
    else:
        default_display = '[Y/n]?'
        default = True

    while 1:
        display = question + '\n' + default_display
        if answer is None:
            log.debug('Under None')
            answer = six.moves.input(display)
        if answer == '':
            log.debug('Under blank')
            return default
        if answer in yes:
            log.debug('Must be true')
            return True
        elif answer in no:
            log.debug('Must be false')
            return False
        else:
            print('Please answer yes or no only!\n\n')
            six.moves.input('Press enter to continue')
            print('\n\n\n\n\n')


def get_correct_answer(question, default=None, required=False,
                       answer=None, is_answer_correct=None):
    while 1:
        if default is None:
            msg = ' - No Default Available'
        else:
            msg = ('\n[DEFAULT] -> {}\nPress Enter To '
                   'Use Default'.format(default))
        prompt = question + msg + '\n--> '
        if answer is None:
            answer = six.moves.input(prompt)
        if answer == '' and required and default is not None:
            print('You have to enter a value\n\n')
            six.moves.input('Press enter to continue')
            print('\n\n')
            answer = None
            continue
        if answer == '' and default is not None:
            answer = default
        _ans = ask_yes_no('You entered {}, is this '
                          'correct?'.format(answer),
                          answer=is_answer_correct)
        if _ans:
            return answer
        else:
            answer = None


# get width and height of console
# works on linux, os x, windows, cygwin(windows)
# originally retrieved from:
# http://stackoverflow.com/questions/566746
def get_terminal_size():
    current_os = platform.system()
    tuple_xy = None
    if current_os == 'Windows':
        tuple_xy = _get_terminal_size_windows()
        if tuple_xy is None:
            tuple_xy = _get_terminal_size_tput()
            # needed for window's python in cygwin's xterm!
    if current_os in ['Linux', 'Darwin'] or current_os.startswith('CYGWIN'):
        tuple_xy = _get_terminal_size_linux()
    if tuple_xy is None:
        print("default")
        tuple_xy = (80, 25)      # default value
    return tuple_xy


def _get_terminal_size_windows():
    try:
        from ctypes import windll, create_string_buffer
        # stdin handle is -10
        # stdout handle is -11
        # stderr handle is -12
        h = windll.kernel32.GetStdHandle(-12)
        csbi = create_string_buffer(22)
        res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
        if res:
            (bufx, bufy, curx, cury, wattr,
             left, top, right, bottom,
             maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
            sizex = right - left + 1
            sizey = bottom - top + 1
            return sizex, sizey
    except:
        pass


# http://stackoverflow.com/questions/263890
def _get_terminal_size_tput():
    # get terminal width
    try:
        cols = int(subprocess.check_call(shlex.split('tput cols')))
        rows = int(subprocess.check_call(shlex.split('tput lines')))
        return (cols, rows)
    except:
        pass


def _get_terminal_size_linux():
    def ioctl_GWINSZ(fd):
        try:
            import fcntl
            # Is this required
            # import termios
            cr = struct.unpack('hh',
                               fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
            return cr
        except:
            pass
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        try:
            cr = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            return None
    return int(cr[1]), int(cr[0])


# Gets a single character form standard input. Does not echo to the screen
class _Getch:

    def __init__(self):
        if sys.platform == 'win32':
            self.impl = _GetchWindows()
        else:
            self.impl = _GetchUnix()

    def __call__(self):
        return self.impl()


class _GetchUnix:
    def __init__(self):
        # Not sure if these imports are required here
        # import tty, sys
        pass

    def __call__(self):
        # NOt sure if these imports are required here
        # import tty, termios
        pass
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        # Not sure if this import is required
        # import msvcrt
        pass

    def __call__(self):
        # Not sure if this import is required
        # import msvcrt
        return msvcrt.getch()
