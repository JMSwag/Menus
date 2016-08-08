from menus import BaseMenu, Engine


class Test(BaseMenu):

    def __init__(self):
        options = [('Jump', self.jump)]
        super(Test, self).__init__(options=options)

    def jump(self):
        raw_input('Jumping!!!')
        self()


if __name__ == '__main__':
    Engine(menus=[Test()]).start()
