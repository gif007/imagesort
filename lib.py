'''
Library of functions for imagesort.py
'''

import os, shutil
from PIL import Image
from tqdm import tqdm
from config import PARAMS
from utils import formatCountDistinction


def validateParams():
    dimensionParams = ['minWidth', 'maxWidth', 'minHeight', 'maxHeight']
    for value in dimensionParams:
        if PARAMS[value]:
            try:
                # Sanitize values which may have been entered as strings
                PARAMS[value] = int(PARAMS[value])
            except ValueError:
                raise Exception('Values must be integers')

            if PARAMS[value] < 0:
                raise Exception('Values must be positive integers')

    if PARAMS['minWidth'] and PARAMS['maxWidth'] and PARAMS['maxWidth'] < PARAMS['minWidth']:
        raise Exception('maxWidth cannot be less than minWidth')
    if PARAMS['minHeight'] and PARAMS['maxHeight'] and PARAMS['maxHeight'] < PARAMS['minHeight']:
        raise Exception('maxHeight cannot be less than minHeight')
    if PARAMS['orientation'] and PARAMS['orientation'] not in ['landscape', 'portrait']:
        raise Exception('Orientation must be "landscape" or "portrait"')


def createResultsDirectory():
    if not os.path.exists('results'):
        try:
            os.mkdir('results')
            if PARAMS['verbose']: print('Created results directory')
        except:
            raise Exception('Failed to create results directory')
    else:
        print('The current directory already contains a directory called "results". Is it okay to use this?')
        response = input('y/n ')
        if not response.lower() == 'y':
            raise Exception('Quitting')


def getAllImages():
    if PARAMS['verbose']: print('Gathering images')

    images = []
    for item in os.listdir():
        try:
            image = Image.open(item)
            images.append((image, item))
        except:
            continue

    if len(images) == 0:
        raise Exception('Could not find images in current directory')
    else:
        return images


def filterImages(images):
    if PARAMS['verbose']: print('Filtering images')

    if PARAMS['orientation']:
        if PARAMS['orientation'] == 'landscape':
            images = [item for item in images if item[0].size[0] > item[0].size[1]]
        elif PARAMS['orientation'] == 'portrait':
            images = [item for item in images if item[0].size[0] < item[0].size[1]]

    if PARAMS['minWidth']:
        images = [item for item in images if item[0].size[0] >= PARAMS['minWidth']]
    if PARAMS['maxWidth']:
        images = [item for item in images if item[0].size[0] <= PARAMS['maxWidth']]
    if PARAMS['minHeight']:
        images = [item for item in images if item[0].size[1] >= PARAMS['minHeight']]
    if PARAMS['maxHeight']:
        images = [item for item in images if item[0].size[1] <= PARAMS['maxHeight']]

    if len(images) == 0:
        raise Exception('All images were filtered out')
    else:
        return images


def copyImagesIntoResults(images):
    count = len(images)
    if count > 0:
        formattedString = formatCountDistinction('image', count)
        print('Copying %d %s into results directory' % (count, formattedString))
        for _, item in tqdm(images):
            shutil.copy(item, 'results')
    else:
        raise Exception('There are no images to move')


def moveImagesIntoResults(images):
    count = len(images)
    if count > 0:
        formattedString = formatCountDistinction('image', count)
        print('Moving %d %s into results directory' % (count, formattedString))
        for _, item in tqdm(images):
            shutil.move(item, 'results')
    else:
        raise Exception('There are no images to move')