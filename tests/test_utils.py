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
import pytest

from menus import MenusError
from menus.utils import clear_screen_cmd, check_options_else_raise


class TestUtils(object):

    def test_clear_screen_cmd(self):
        assert clear_screen_cmd == 'clear'

    def test_check_options_else_raise(self):
        assert check_options_else_raise([('Menu', 'First')]) is True

    def test_check_optiosn_else_rasie_fail_no_tuple(self):
        with pytest.raises(MenusError):
            check_options_else_raise(['Menu', 'First'])

    def test_check_optiosn_else_rasie_fail_greater_10(self):
        with pytest.raises(MenusError):
            data = [('Menu', 'First'), ('Menu', 'First'), ('Menu', 'First'),
                    ('Menu', 'First'), ('Menu', 'First'), ('Menu', 'First'),
                    ('Menu', 'First'), ('Menu', 'First'), ('Menu', 'First'),
                    ('Menu', 'First'),]
            check_options_else_raise(data)

    def test_check_optiosn_else_rasie_fail_string(self):
        with pytest.raises(MenusError):
            check_options_else_raise([(112, 'First')])
