import unittest

from src.si_prefix import normalize_value, round_to_nearest_known_prefix_power, build_si_prefix


class TestSiPrefix(unittest.TestCase):

    def test_normalize_value(self):
        test_cases = [
            # Positive >= 1
            {'input': 1, 'expected': (1, 0)},
            {'input': 1.2, 'expected': (1.2, 0)},
            {'input': 10, 'expected': (1, 1)},
            {'input': 12.3, 'expected': (1.23, 1)},
            {'input': 100, 'expected': (1, 2)},
            {'input': 123, 'expected': (1.23, 2)},
            # Negative <= -1
            {'input': -1, 'expected': (-1, 0)},
            {'input': -1.2, 'expected': (-1.2, 0)},
            {'input': -10, 'expected': (-1, 1)},
            {'input': -12.3, 'expected': (-1.23, 1)},
            {'input': -100, 'expected': (-1, 2)},
            {'input': -123, 'expected': (-1.23, 2)},
            # Positive fractions
            {'input': 0.1, 'expected': (1, -1)},
            {'input': 0.12, 'expected': (1.2, -1)},
            {'input': 0.01, 'expected': (1, -2)},
            {'input': 0.012, 'expected': (1.2, -2)},
            {'input': 0.001, 'expected': (1, -3)},
            {'input': 0.00123, 'expected': (1.23, -3)},
            # Negative fractions
            {'input': -0.1, 'expected': (-1, -1)},
            {'input': -0.12, 'expected': (-1.2, -1)},
            {'input': -0.01, 'expected': (-1, -2)},
            {'input': -0.012, 'expected': (-1.2, -2)},
            {'input': -0.001, 'expected': (-1, -3)},
            {'input': -0.00123, 'expected': (-1.23, -3)},
            # Edge cases
            {'input': 0, 'expected': (0, 0)},
        ]

        for test_case in test_cases:
            result = normalize_value(test_case['input'])
            self.assertEqual(test_case['expected'], result, f"For {test_case['input']}")

    def test_round_to_nearest_known_prefix_power(self):
        test_cases = [
            {'input': (1.2, -27), 'expected': (0.0012, -24)},
            {'input': (1.2, -26), 'expected': (0.012, -24)},
            {'input': (1.2, -25), 'expected': (0.12, -24)},
            {'input': (1.2, -24), 'expected': (1.2, -24)},
            {'input': (1.2, -9), 'expected': (1.2, -9)},
            {'input': (1.2, -8), 'expected': (12, -9)},
            {'input': (1.2, -7), 'expected': (120, -9)},
            {'input': (1.2, -6), 'expected': (1.2, -6)},
            {'input': (1.2, -5), 'expected': (12, -6)},
            {'input': (1.2, -4), 'expected': (120, -6)},
            {'input': (1.2, -3), 'expected': (1.2, -3)},
            {'input': (1.2, -2), 'expected': (1.2, -2)},
            {'input': (1.2, -1), 'expected': (1.2, -1)},
            {'input': (1.2, 0), 'expected': (1.2, 0)},
            {'input': (1.2, 1), 'expected': (1.2, 1)},
            {'input': (1.2, 2), 'expected': (1.2, 2)},
            {'input': (1.2, 3), 'expected': (1.2, 3)},
            {'input': (1.2, 4), 'expected': (12, 3)},
            {'input': (1.2, 5), 'expected': (120, 3)},
            {'input': (1.2, 6), 'expected': (1.2, 6)},
            {'input': (1.2, 7), 'expected': (12, 6)},
            {'input': (1.2, 8), 'expected': (120, 6)},
            {'input': (1.2, 9), 'expected': (1.2, 9)},
            {'input': (1.2, 24), 'expected': (1.2, 24)},
            {'input': (1.2, 25), 'expected': (12, 24)},
            {'input': (1.2, 26), 'expected': (120, 24)},
            {'input': (1.2, 27), 'expected': (1200, 24)},
        ]
        for test_case in test_cases:
            result = round_to_nearest_known_prefix_power(*test_case['input'])
            self.assertEqual(test_case['expected'], result, f"For {test_case['input']}")

    def test_build_si_prefix(self):
        test_cases = [
            {
                'input': (12.7, 3, 'g'),
                'expected': {
                    'value': 12.7,
                    'formatted': '12.7 kg',
                    'prefix': {
                        'name': 'kilo',
                        'symbol': 'k',
                        'power': 3,
                        'word': 'thousand'
                    }
                }
            },
            {
                'input': (15, 0),
                'expected': {
                    'value': 15,
                    'formatted': '15',
                    'prefix': {
                        'name': '',
                        'symbol': '',
                        'power': 0,
                        'word': 'one'
                    }
                }
            },
        ]
        for test_case in test_cases:
            result = build_si_prefix(*test_case['input'])
            self.assertEqual(test_case['expected'], result, f"For {test_case['input']}")
