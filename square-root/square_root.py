# binary search - significantly faster than the #first attempt

def square_root(number):
    if number == 1: return 1
    left = 1
    right = number // 2
    while left <= right:
        middle_element = (left + right) // 2
        if middle_element * middle_element == number:
            return middle_element
        elif middle_element * middle_element < number:
            left = middle_element + 1
        else:
            right = middle_element - 1 
    return f"No natural square root"

# first attempt

# def square_root_slow(number):
#     for i in range(1, number + 1):
#         if i * i == number:
#             return i
#     return None

# import cProfile
# cProfile.run('square_root_slow(1000000000)')

# cProfile.run('square_root(1000000000)')