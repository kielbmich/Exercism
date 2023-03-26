def is_pangram(sentence):
    alphabet = set(map(chr, range(ord("a"), ord("z") + 1)))
    for letter in sentence:
        if letter.lower() in alphabet:
            alphabet -= set(letter.lower())
    return True if len(alphabet) == 0 else False

