import unittest

from src.convert_length import convert_length


class TestConvertLength(unittest.TestCase):

    def test_convert_length(self):
        test_cases = [
            {'input': 10.45, 'from': 'centimeter', 'to': 'inch', 'expected': 4.1141732283},
            {'input': 2.24, 'from': 'meter', 'to': 'yard', 'expected': 2.4496937883},
            {'input': 9.1, 'from': 'foot', 'to': 'meter', 'expected': 2.77368},
            {'input': 10, 'from': 'meter', 'to': 'meter', 'expected': 10},
        ]

        for test_case in test_cases:
            result = convert_length(test_case['input'], test_case['from'], test_case['to'])
            self.assertAlmostEqual(test_case['expected'], result, places=3, msg=f"For {test_case['input']}")
