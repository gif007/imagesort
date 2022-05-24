import sys, os, shutil
from PIL import Image
from tqdm import tqdm
from config import PARAMS

def validateParams():
    if PARAMS['minWidth'] and PARAMS['maxWidth'] and PARAMS['maxWidth'] < PARAMS['minWidth']:
        print('maxWidth cannot be less than minWidth')
        sys.exit()

    if PARAMS['minHeight'] and PARAMS['maxHeight'] and PARAMS['maxHeight'] < PARAMS['minHeight']:
        print('maxHeight cannot be less than minHeight')
        sys.exit()

    for value in [PARAMS['minWidth'], PARAMS['maxWidth'], PARAMS['minHeight'], PARAMS['maxHeight']]:
        if value and value < 0:
            print('Values must be positive integers')
            sys.exit()

    if PARAMS['orientation'] and PARAMS['orientation'] not in ['landscape', 'portrait']:
        print('Orientation must be landscape or portrait')
        sys.exit()


def createResultsDirectory():
    if not os.path.exists('results'):
        try:
            os.mkdir('results')
            if PARAMS['verbose']: print('Created results directory')
        except:
            print('Failed to create results directory')
            sys.exit()
    else:
        print('The current directory already contains a directory called "results". Is it okay to use this?')
        response = input('y/n ')
        if not response.lower() == 'y':
            print('Complete')
            sys.exit()


def getAllImages():
    if PARAMS['verbose']: print('Gathering images')
    images = []
    for item in os.listdir():
        try:
            image = Image.open(item)
        except:
            continue
        else:
            images.append((image, item))
        
    if len(images) == 0:
        print('Could not find images in current directory')
        sys.exit()
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

    return images


def copyImagesIntoResults(images):
    if len(images) > 0:
        print('Copying %d image(s) into results directory' % len(images))
        for _, item in tqdm(images):
            shutil.copy(item, 'results')
        if PARAMS['verbose']: print('Complete')