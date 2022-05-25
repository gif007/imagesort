#!/bin/python

"""
Finds all images in the current working directory,
filters them and copies them into a subdirectory
"""

import sys, platform, subprocess
from lib import *


if __name__ == '__main__':
    try:
        validateParams()
        createResultsDirectory()
        images = filterImages(getAllImages())
        copyImagesIntoResults(images)
        if platform.system() == 'Linux':
            subprocess.run(['notify-send', 'ImageSort has finished copying %d image(s)' % len(images)])
    except Exception as exc:
        print(exc)
        if platform.system() == 'Linux':
            subprocess.run(['notify-send', 'ImageSort: %s' % exc])
        sys.exit()