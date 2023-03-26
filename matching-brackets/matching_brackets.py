def is_paired(input_string):
    only_braces = pop_elements(input_string)
    if only_braces == False:
        return False
    inn = check_function(only_braces)
    for i in range(10):
        inn = check_function(only_braces)
    return True if inn[0] == "" else False

def pop_elements(input_string):
    check = ""
    for letter in input_string:
        if letter in "{}()[]":
            check += letter
    if len(check) % 2 != 0:
        return False
    return check

def check_function(check):
    change = False
    for char_i in check:
        for char_j in check:
            if char_i == "(" and char_j == ")" or char_i == "[" and char_j == "]" or char_i == "{" and char_j == "}":
                check = check.replace(char_i, "X").replace(char_j, "X")
                return [check, True]
    return [check, False]

check_function("({([]}")

"{[]}".replace("{","")
