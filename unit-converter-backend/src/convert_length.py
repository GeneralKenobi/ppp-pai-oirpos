def convert_length(value, from_unit, to_unit):
    if from_unit not in ratios_to_meter:
        raise f"{from_unit} is not a known unit"
    if to_unit not in ratios_from_meter:
        raise f"{to_unit} is not a known unit"

    ratio = ratios_to_meter[from_unit] * ratios_from_meter[to_unit]
    return {'value': value * ratio}


ratios_to_meter = {
    'centimeter': 0.01,
    'meter': 1,
    'kilometer': 1000,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.35
}

ratios_from_meter = {
    'centimeter': 100,
    'meter': 1,
    'kilometer': 0.001,
    'inch': 39.37007874,
    'foot': 3.280839895,
    'yard': 1.0936132983,
    'mile': 0.0006213689
}
