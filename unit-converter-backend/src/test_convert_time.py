import unittest

from src.convert_time import convert_time


class TestConvertTime(unittest.TestCase):

    def test_convert_time(self):
        test_cases = [
            {'input': 123.1, 'from': 'hour', 'to': 'minute', 'expected': 7386},
            {'input': 214.2, 'from': 'hour', 'to': 'second', 'expected': 771120},
            {'input': 339.1, 'from': 'second', 'to': 'day', 'expected': 0.0039247685},
            {'input': 10, 'from': 'second', 'to': 'second', 'expected': 10},
        ]

        for test_case in test_cases:
            result = convert_time(test_case['input'], test_case['from'], test_case['to'])
            self.assertAlmostEqual(test_case['expected'], result, places=3, msg=f"For {test_case['input']}")
