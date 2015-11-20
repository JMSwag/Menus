from __future__ import print_function

import os
import shutil

from jms_utils.paths import ChDir

HTML_DIR = os.path.join(os.getcwd(), 'site')
DEST_DIR = os.path.join(os.path.expanduser(u'~'), u'BTSync',
                        u'code', u'Web', u'Menus')


def main():
    with ChDir(DEST_DIR):
        files = os.listdir(os.getcwd())
        for f in files:
            if f.startswith(u'.'):
                continue
            elif f in [u'Procfile', 'Staticfile']:
                continue
            elif os.path.isfile(f):
                os.remove(f)
            elif os.path.isdir(f):
                shutil.rmtree(f, ignore_errors=True)

    with ChDir(HTML_DIR):
        files = os.listdir(os.getcwd())
        for f in files:
            if f.startswith(u'.'):
                continue
            if os.path.isfile(f):
                shutil.copy(f, os.path.join(DEST_DIR, f))
            elif os.path.isdir(f):
                shutil.copytree(f, DEST_DIR + os.sep + f)

if __name__ == '__main__':
    main()
    print(u'Move complete')
