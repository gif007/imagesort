#!/bin/python

"""
Finds all  images in the current working directory
and filters them and copies them into a subdirectory
"""

from utils import *


if __name__ == '__main__':
    validateParams()
    createResultsDirectory()
    images = filterImages(getAllImages())
    copyImagesIntoResults(images)