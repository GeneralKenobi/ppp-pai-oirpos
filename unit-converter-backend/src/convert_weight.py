def convert_weight(value, from_unit, to_unit):
    if from_unit not in ratios_to_gram:
        raise f"{from_unit} is not a known unit"
    if to_unit not in ratios_from_gram:
        raise f"{to_unit} is not a known unit"

    ratio = ratios_to_gram[from_unit] * ratios_from_gram[to_unit]
    return {'value': value * ratio}


ratios_to_gram = {
    'gram': 1,
    'kilogram': 1000,
    'ton': 1000000,
    'ounce': 28.3495,
    'pound': 4127.6872
}

ratios_from_gram = {
    'gram': 1,
    'kilogram': 0.001,
    'ton': 0.000001,
    'ounce': 0.0352739907,
    'pound': 0.0022046244
}
