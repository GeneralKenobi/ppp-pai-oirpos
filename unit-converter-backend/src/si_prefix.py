import math


def si_prefix(value, unit=None):
    value, power = normalize_value(value)
    value, power = round_to_nearest_known_prefix_power(value, power)
    return build_si_prefix(value, power, unit)


def normalize_value(value):
    if value == 0:
        return 0, 0

    is_negative = value < 0
    value = math.fabs(value)

    # 123      -> 2.  -> 2
    # 12345678 -> 7.  -> 7
    # 1.5      -> 0.  -> 0
    # 0.000123 -> -4. -> -4
    # 10       -> 1   -> 1
    power_of_10 = math.log10(value)
    power_of_10 = math.floor(power_of_10)

    value /= math.pow(10, power_of_10)
    if is_negative:
        value = -value

    return value, power_of_10


def round_to_nearest_known_prefix_power(value, power):
    if power <= -24:
        value *= math.pow(10, power + 24)
        return value, -24
    if power >= 24:
        value *= math.pow(10, power - 24)
        return value, 24

    known_prefix_powers = [-24, -21, -18, -15, -12, -9, -6, -3, -2, -1, 0, 1, 2, 3, 6, 9, 12, 15, 18, 21, 24]
    while power not in known_prefix_powers:
        power -= 1
        value *= 10

    return value, power


def build_si_prefix(value, power, unit=None):
    if unit is None:
        unit = ""

    prefix = prefixes[power]
    return {
        'value': value,
        'formatted': f"{value} {prefix['symbol']}{unit}".strip(),
        'prefix': {
            'name': prefix['name'],
            'symbol': prefix['symbol'],
            'power': prefix['power'],
            'word': prefix['word']
        }
    }


prefixes = {
    -24: {
        'name': 'yocto',
        'symbol': 'y',
        'power': -24,
        'word': 'septillionth'
    },
    -21: {
        'name': 'zepto',
        'symbol': 'z',
        'power': -21,
        'word': 'sextillionth'
    },
    -18: {
        'name': 'atto',
        'symbol': 'a',
        'power': -18,
        'word': 'quintillionth'
    },
    -15: {
        'name': 'femto',
        'symbol': 'f',
        'power': -15,
        'word': 'quadrillionth'
    },
    -12: {
        'name': 'pico',
        'symbol': 'p',
        'power': -12,
        'word': 'trillionth'
    },
    -9: {
        'name': 'nano',
        'symbol': 'n',
        'power': 9,
        'word': 'billionth'
    },
    -6: {
        'name': 'micro',
        'symbol': 'mu',
        'power': -6,
        'word': 'millionth'
    },
    -3: {
        'name': 'milli',
        'symbol': 'm',
        'power': -3,
        'word': 'thousandth'
    },
    -2: {
        'name': 'centi',
        'symbol': 'c',
        'power': -2,
        'word': 'hundredth'
    },
    -1: {
        'name': 'deci',
        'symbol': 'd',
        'power': -1,
        'word': 'tenth'
    },
    0: {
        'name': '',
        'symbol': '',
        'power': 0,
        'word': 'one'
    },
    1: {
        'name': 'deka',
        'symbol': 'da',
        'power': 1,
        'word': 'ten'
    },
    2: {
        'name': 'hecto',
        'symbol': 'h',
        'power': 2,
        'word': 'hundred'
    },
    3: {
        'name': 'kilo',
        'symbol': 'k',
        'power': 3,
        'word': 'thousand'
    },
    6: {
        'name': 'mega',
        'symbol': 'M',
        'power': 6,
        'word': 'million'
    },
    9: {
        'name': 'giga',
        'symbol': 'G',
        'power': 9,
        'word': 'billion'
    },
    12: {
        'name': 'tera',
        'symbol': 'T',
        'power': 12,
        'word': 'trillion'
    },
    15: {
        'name': 'peta',
        'symbol': 'P',
        'power': 15,
        'word': 'quadrillion'
    },
    18: {
        'name': 'exa',
        'symbol': 'E',
        'power': 18,
        'word': 'quintillion'
    },
    21: {
        'name': 'zetta',
        'symbol': 'Z',
        'power': 21,
        'word': 'sextillion'
    },
    24: {
        'name': 'yotta',
        'symbol': 'Y',
        'power': 24,
        'word': 'septillion'
    },
}
