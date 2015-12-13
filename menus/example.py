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

from menus.utils import BaseMenu


log = logging.getLogger(__name__)


class Cool(BaseMenu):

    def __init__(self):
        options = [('Speak', self.speak)]
        super(Cool, self).__init__(options=options)

    def speak(self):
        self.display_msg("Pass me a blanket.")
        six.moves.input()
        self()


class Hot(BaseMenu):

    def __init__(self):
        options = [('Speak', self.speak)]
        super(Hot, self).__init__(options=options)

    def speak(self):
        self.display_msg("It's getting hot in here!")
        six.moves.input()
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
        six.moves.input()
        self()

examples = [Cool(), Hot(), Keys()]
