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

from menus import BaseMenu, MenusError
from menus.engine import check_mro, Engine


class TestEngine(object):

    def test_engine_defaults(self):
        engine = Engine(example=True)
        assert engine.main.app_name == 'ACME'


class TestMRO(object):

    def test_mro_fail(self):
        class MyMenu(object): pass

        my_menu = MyMenu()

        with pytest.raises(MenusError):
            check_mro(my_menu)

    def test_mro(self):
        class MyMenu(BaseMenu):
            def __init__(self, *args, **kwargs):
                super(MyMenu, self).__init__(*args, **kwargs)

        my_menu = MyMenu()
        assert check_mro(my_menu) is True
