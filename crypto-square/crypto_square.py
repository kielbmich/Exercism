from math import ceil, sqrt
def normalize(plain_text):
    return "".join([l.lower() for l in plain_text if (l.isalpha() or l.isnumeric())])

def rectangle(text):
    c = r = ceil(sqrt(len(text)))
    if c * (r - 1) >= len(text):
        return c, r - 1
    return c, r
    
def cipher_text(plain_text):
    text = normalize(plain_text)
    c, r = rectangle(text)
    text = text.ljust(c * r)
    text_divided = [text[i : i + c] for i in range(0, r * (c - 1) + 1, 1 if c == 0 else c)]
    text_out = [""] * c
    for word in text_divided:
        for i in range(c):
            text_out[i] += word[i] 
    return " ".join(text_out)

cipher_text("If man was meant to stay on the ground, god would have given us roots.")
cipher_text("Chill out.")
cipher_text("This is fun!")
