#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys

NEST = shutil.which('drongo-nest')


def run_dev():
    os.environ['DRONGO_SETTINGS_FILE'] = os.path.realpath(sys.argv[1])
    app = subprocess.Popen(
        ['python', '-m', 'nest.cmd', 'drongo_app.app:app', '--auto-reload'])

    try:
        app.wait()
    except KeyboardInterrupt:
        print('Terminating...')
        app.terminate()
        app.wait()


def run():
    os.environ['DRONGO_SETTINGS_FILE'] = os.path.realpath(sys.argv[1])
    app = subprocess.Popen(
        ['python', '-m', 'nest.cmd', 'drongo_app.app:app'])

    try:
        app.wait()
    except KeyboardInterrupt:
        print('Terminating...')
        app.terminate()
        app.wait()
