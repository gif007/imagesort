#!/bin/python

"""
Finds all images in the current working directory,
filters them and moves them into a subdirectory
"""

import sys, platform, subprocess
from lib import *
from utils import formatCountDistinction


HELP_MESSAGE = """ImageSort will filter all of the images in the current \
directory into a subdirectory called "results" based on dimensions.
See "config.py" to get started."""

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        if args[0] in ['-h', '--help']:
            print(HELP_MESSAGE)
        sys.exit()

    try:
        validateParams()
        images = filterImages(getAllImages())
        createResultsDirectory()
        moveImagesIntoResults(images)

        if platform.system() == 'Linux':
            count = len(images)
            formattedString = formatCountDistinction('image', count)
            subprocess.run(['notify-send', 'ImageSort has finished moving %d %s' % (count, formattedString)])
            
    except Exception as exc:
        print(exc)
        if platform.system() == 'Linux':
            subprocess.run(['notify-send', 'ImageSort: %s' % exc])
        sys.exit()