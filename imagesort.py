#!/bin/python

"""
Finds all  images in the current working directory
and filters them and copies them into a subdirectory
"""

import sys
from utils import *


if __name__ == '__main__':
    try:
        validateParams()
    except Exception as exc:
        print(exc)
        sys.exit()
        
    try:
        createResultsDirectory()
    except Exception as exc:
        print(exc)
        sys.exit()

    try:
        images = getAllImages()
    except Exception as exc:
        print(exc)
        sys.exit()

    images = filterImages(images)
    copyImagesIntoResults(images)