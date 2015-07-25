import os
import shutil
import sys


class ChDir(object):

    def __init__(self, goto):
        self.goto = goto
        self.old_dir = os.getcwd()

    def __enter__(self, *args, **kwargs):
        os.chdir(self.goto)

    def __exit__(self, *args, **kwargs):
        os.chdir(self.old_dir)


def deploy(sub_cmd=None):
    if sub_cmd is None:
        version = raw_input('Enter version\n--> ')
    else:
        version = sub_cmd
    cmds = ['git tag {}'.format(version),
            'python setup.py sdist bdist_wheel',
            'twine upload dist/*']
    for c in cmds:
        os.system(c)
    remove_dist()


def remove_dist(sub_cmd=None):
    with ChDir(u'dist'):
        files = os.listdir(os.getcwd())
        for f in files:
            if u'.DS' in f:
                continue
            elif os.path.isfile(f) is True:
                os.remove(f)
            elif os.path.isdir(f) is True:
                shutil.rmtree(f, ignore_errors=True)

commands = {
    'deploy': deploy,
    'remove_dist': remove_dist,
}


def main():
    try:
        cmd = sys.argv[1]
        try:
            sub_cmd = sys.argv[2]
        except IndexError:
            sub_cmd = None
        if cmd not in commands.keys():
            sys.exit(u'Not a valid command:\n\nAvailable '
                     u'commands\n{}'.format(' '.join(commands.keys())))
        else:
            commands[cmd](sub_cmd)
    except IndexError:
        sys.exit(u'You must pass a command')


if __name__ == '__main__':
    main()
