'''
Utility functions for imagesort.py
'''

def formatCountDistinction(wrd, num):
    """
    First draft of a function which formats the spelling of a word
    to be either singular or plural
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    normal = (wrd.endswith('y') and wrd[-2] in vowels) or not wrd.endswith('y')

    if num > 1:
        if normal:
            return wrd + 's'
        else:
            wrd = wrd[:-1]
            return wrd + 'ies'
    else:
        return wrd