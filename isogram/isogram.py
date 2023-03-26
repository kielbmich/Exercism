def is_isogram(string):
    out = ""
    for letter in string:
        if letter.isalpha():
            if letter.lower() in out:
                return False
            else:
                out += letter.lower()
    return True

