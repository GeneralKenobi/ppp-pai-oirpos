def convert_time(value, from_unit, to_unit):
    if from_unit not in ratios_to_second:
        raise f"{from_unit} is not a known unit"
    if to_unit not in ratios_from_second:
        raise f"{to_unit} is not a known unit"

    ratio = ratios_to_second[from_unit] * ratios_from_second[to_unit]
    return {'value': value * ratio}


ratios_to_second = {
    'second': 1,
    'minute': 60,
    'hour': 60 * 60,
    'day': 24 * 60 * 60,
}

ratios_from_second = {
    'second': 1,
    'minute': 0.0166666667,
    'hour': 0.0002777778,
    'day': 0.0000115741,
}
