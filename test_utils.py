import unittest
from utils import formatCountDistinction as fcd


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