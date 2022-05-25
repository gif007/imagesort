'''
Utility functions for imagesort.py
'''

def formatCountDistinction(wrd, num):
    """
    Formats the spelling of a word to be either singular or plural
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    normal = (wrd.endswith('y') and wrd[-2] in vowels) or not wrd.endswith('y')

    if num != 1:
        if normal:
            return wrd + 's'
        else:
            wrd = wrd[:-1]
            return wrd + 'ies'
    else:
        return wrd

if __name__ == '__main__':
    import unittest
    fcd = formatCountDistinction

    class TestUtils(unittest.TestCase):

        def test_formatting_plural(self):
            self.assertEqual(fcd('image', 0), 'images')
            self.assertEqual(fcd('image', 42), 'images')
            self.assertEqual(fcd('image', -42), 'images')

        def test_formatting_singular(self):
            self.assertEqual(fcd('image', 1), 'image')

        def test_formatting_plural_words_ending_in_y(self):
            self.assertEqual(fcd('monkey', 0), 'monkeys')
            self.assertEqual(fcd('monkey', 42), 'monkeys')
            self.assertEqual(fcd('monkey', -42), 'monkeys')
            self.assertEqual(fcd('candy', 0), 'candies')
            self.assertEqual(fcd('candy', 42), 'candies')
            self.assertEqual(fcd('candy', -42), 'candies')

        def test_formatting_singular_words_ending_in_y(self):
            self.assertEqual(fcd('monkey', 1), 'monkey')
            self.assertEqual(fcd('candy', 1), 'candy')

    unittest.main()