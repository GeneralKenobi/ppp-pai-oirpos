import unittest

from src.convert_weight import convert_weight


class TestConvertWeight(unittest.TestCase):

    def test_convert_weight(self):
        test_cases = [
            {'input': 12345, 'from': 'kilogram', 'to': 'ton', 'expected': 12.345},
            {'input': 23.41, 'from': 'gram', 'to': 'pound', 'expected': 0.0516102577},
            {'input': 110.21, 'from': 'ounce', 'to': 'gram', 'expected': 3124.398395},
            {'input': 10, 'from': 'gram', 'to': 'gram', 'expected': 10},
        ]

        for test_case in test_cases:
            result = convert_weight(test_case['input'], test_case['from'], test_case['to'])
            self.assertAlmostEqual(test_case['expected'], result, places=3, msg=f"For {test_case['input']}")
