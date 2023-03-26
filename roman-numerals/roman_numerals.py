translate = {
    1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X",
    40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 
    500: "D", 900: "CM", 1000: "M"
    }

def roman(number): 
    out = ""
    for i in sorted(translate.keys(), reverse = True):
        multiplier = number // i
        out += multiplier * translate.get(i)
        number %= i
    return out


# some faulty roman -> arabic function here

# import random

# translate = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}

# def roman_arabic(number):
#     out = 0
#     for i in range(len(number)):
#         if i == (len(number) - 1):
#             out += translate.get(number[-1])
#         elif translate.get(number[i + 1]) <= translate.get(number[i]):
#             out += translate.get(number[i])
#         else:
#             out -= translate.get(number[i])
#     return out

# guessing the roman basing on roman -> arabic function

# def arabic_roman(number):
#     match = False
#     while not match:
#         guess = "".join(random.choice("IVXLCDM") for i in range(random.randint(1, 9)))
#         if roman_arabic(guess) == number:
#             match = True
#     return guess