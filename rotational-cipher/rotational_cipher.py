def rotate(text, key):
    alphabet = "".join(list(map(chr, range(97,123))))
    rotated_alphabet = alphabet[key:] + alphabet[:key]
    translation_table = "".maketrans(alphabet + alphabet.upper(), rotated_alphabet + rotated_alphabet.upper())
    return text.translate(translation_table)