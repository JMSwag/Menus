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


class TestBaseMenu(object):

    def test_base_menu_defaults(self):
        base_menu = BaseMenu()
        assert base_menu.menu_name == 'BaseMenu'
        assert len(base_menu.commands) == 0
        assert base_menu.message is None


class TestBaseMenuPauseMethods(object):

    def test_enter_fail_string(self):
        with pytest.raises(MenusError):
            base_menu = BaseMenu()
            base_menu.pause(enter_to_continue='test')

    def test_enter_fail_number(self):
        with pytest.raises(MenusError):
            base_menu = BaseMenu()
            base_menu.pause(enter_to_continue=5)

    def test_seconds_fail_string(self):
        with pytest.raises(MenusError):
            base_menu = BaseMenu()
            base_menu.pause(seconds='5')

    def test_pause_method(self):
        base_menu = BaseMenu()
        assert base_menu.pause(seconds=1) is True


class TestMyMenu(object):

    def test_subclass_menu_defaults(self):
        class MyMenu(BaseMenu):
            def __init__(self, *args, **kwargs):
                super(MyMenu, self).__init__(*args, **kwargs)

        my_menu = MyMenu()
        assert my_menu.menu_name == 'MyMenu'
        assert len(my_menu.commands) == 0
        assert my_menu.message is None

    def test_subclass_menu_options_deprecated(self):
        class MyMenu(BaseMenu):

            def __init__(self, *args, **kwargs):
                options = [('Speak', self.speak)]
                super(MyMenu, self).__init__(options=options)

            def speak(self):
                print('Hi from MyMenu')

        my_menu = MyMenu()
        assert my_menu.menu_name == 'MyMenu'
        assert len(my_menu.commands) == 1
        assert my_menu.message is None

    def test_subclass_menu_command_options_mix(self):
        class MyMenu(BaseMenu):

            def __init__(self, *args, **kwargs):
                options = [('Speak', self.speak)]
                super(MyMenu, self).__init__(options=options,
                                             commands=options)

            def speak(self):
                print('Hi from MyMenu')

        with pytest.raises(MenusError):
            MyMenu()

    def test_custom_name(self):
        custom_menu = BaseMenu(menu_name='CustomMenu')
        assert custom_menu.menu_name == 'CustomMenu'
