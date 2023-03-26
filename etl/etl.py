def transform(legacy_data):
    empty_dict = {}
    for key, value in legacy_data.items():
        for letter in value:
            empty_dict[letter.lower()] = key
    return empty_dict
