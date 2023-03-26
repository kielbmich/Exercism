from string import ascii_lowercase as letters
import secrets

class Cipher:
    

    def __init__(self, key = None):
        if key and (key.islower() and key.isalpha()):
            self.key = key
        else:
            self.key = "".join((secrets.choice(letters) for _ in range(100)))
        self.key_len = len(self.key)
    
    def encode_decode(self, text, direction):
        out = []
        for i, c in enumerate(text):
            chr_position = letters.index(c) 
            shift_margin = letters.index(self.key[i % self.key_len])
            out.append(letters[(chr_position + direction * shift_margin) % 26])
        return out

    # def encode_decode(self, text, direction):
    #     return [letters[(letters.index(c) + direction * letters.index(self.key[i % self.key_len])) % 26] for i, c in enumerate(text)]

    def encode(self, plaintext):        
        return "".join(self.encode_decode(plaintext, 1))

    def decode(self, encodedtext):  
        return "".join(self.encode_decode(encodedtext, -1))
