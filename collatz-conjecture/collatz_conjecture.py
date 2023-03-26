def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    i = 0
    while number > 1:
        number = number / 2 if number % 2 == 0 else 3 * number + 1
        i += 1
    return i