import math
def classify(number):
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    accumulate = 0
    for i in range(1, math.floor(number/2) + 1):
        if number % i == 0:
            accumulate += i
    if accumulate > number:
        return "abundant"
    return "perfect" if accumulate == number else "deficient"