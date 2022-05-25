import unittest
from config import PARAMS
from lib import validateParams


class TestLib(unittest.TestCase):

    def setUp(self):
        for value in ['orientation', 'minWidth', 'maxWidth', 'minHeight', 'maxHeight']:
            PARAMS[value] = None
        PARAMS['verbose'] = False

    def test_it_validates_correct_orientation(self):
        PARAMS['orientation'] = 'landscape'
        validateParams()

    def test_it_throws_with_incorrect_orientation(self):
        PARAMS['orientation'] = 'hello world'
        with self.assertRaises(Exception):
            validateParams()

    def test_it_validates_integer_values(self):
        PARAMS['minWidth'] = '42'
        PARAMS['maxWidth'] = 84
        PARAMS['minHeight'] = '42'
        PARAMS['maxHeight'] = 84
        validateParams()

    def test_it_throws_with_noninteger_values(self):
        PARAMS['minWidth'] = 'abc'
        with self.assertRaises(Exception):
            validateParams()

    def test__it_throws_with_illogical_width_dimensions(self):
        PARAMS['minWidth'] = 100
        PARAMS['maxWidth'] = 50
        with self.assertRaises(Exception):
            validateParams()

    def test__it_validates_with_logical_width_dimensions(self):
        PARAMS['minWidth'] = 100
        PARAMS['maxWidth'] = 500
        validateParams()

    def test__it_throws_with_illogical_height_dimensions(self):
        PARAMS['minHeight'] = 100
        PARAMS['maxHeight'] = 50
        with self.assertRaises(Exception):
            validateParams()

    def test__it_validates_with_logical_height_dimensions(self):
        PARAMS['minHeight'] = 100
        PARAMS['maxHeight'] = 500
        validateParams()

    def test_it_throws_with_negative_dimensions(self):
        PARAMS['minHeight'] = -100
        with self.assertRaises(Exception):
            validateParams()


if __name__ == '__main__':
    unittest.main()