plain = "".join(list(map(chr, range(97, 123)))) + "".join(list(map(chr, range(97, 123)))).upper()
cipher = "".join(list(map(chr, range(97, 123))))[::-1]*2

def encode(plain_text):
    out = ""
    count = 0
    to_change_spaces = plain_text.translate(str.maketrans(plain, cipher, " ,."))
    for character in to_change_spaces:
        if character.isalpha() or character.isnumeric():
            count += 1
        if count % 5 != 0:
            out += character
        if count % 5 == 0:
            out += character + " "
    return out.rstrip()

def decode(ciphered_text):
    return ciphered_text.translate(str.maketrans(cipher[0:26], plain[0:26], " "))