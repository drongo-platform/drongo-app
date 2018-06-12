#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

NEST = shutil.which('drongo-nest')


def run_dev():
    os.environ['DRONGO_SETTINGS_FILE'] = os.path.realpath(sys.argv[1])
    from nest import Nest
    from drongo_app.app import app

    server = Nest(app=app, auto_reload=True)
    try:
        server.run()
    except KeyboardInterrupt:
        print('Terminating...')
        server.shutdown()


def run():
    os.environ['DRONGO_SETTINGS_FILE'] = os.path.realpath(sys.argv[1])
    server = Nest(app=app)

    try:
        server.run()
    except KeyboardInterrupt:
        print('Terminating...')
        server.shutdown()


if __name__ == '__main__':
    run()
