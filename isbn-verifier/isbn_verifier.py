from traceback import print_tb


def is_valid(isbn):
    isbn = [char for char in isbn if char != "-"]
    if not len(isbn) == 10 or not (isbn[-1].isnumeric() or isbn[-1] == "X"):
        return False
    isbn[-1] = 10 if isbn[-1] == "X" else isbn[-1]
    for char in isbn[:-1]:
        if str(char).isalpha():
            return False
    weights = range(10, 0, -1)
    sum_prod = 0
    for weight, number in zip(weights, isbn):
        sum_prod += weight * int(number)
    return sum_prod % 11 == 0
