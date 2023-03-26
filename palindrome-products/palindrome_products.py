def is_palindrome(number):
    return str(number) == str(number)[::-1]

def test_palindrome(i, j, palindrome, order):
    if palindrome == None:
        return False 
    if (order == 1 and i*j < palindrome) or (order == -1 and i*j > palindrome):
        return 1 #Better than the previous palindrome
    if (order == 1 and i*i > palindrome) or (order == -1 and i*i < palindrome):
        return 2 #Best possible palindrome
    return None

def analitics(max_factor, min_factor, order):
    factors = []
    palindrome = None
    for i in range(min_factor, max_factor, order):
        for j in range(i, max_factor, order):
            if is_palindrome(i*j):
                if not palindrome:
                    palindrome = i*j
                    factors = [[i,j]]
                elif i*j == palindrome:
                    factors.append([i,j])
                if test_palindrome(i, j, palindrome, order) == 1: #"Better than the previous palindrome"
                    palindrome = i*j
                    factors = [[i,j]]
            if palindrome and i*j < palindrome:
                break
        if test_palindrome(i, i, palindrome, order) == 2: #Best possible palindrome
            break
    return (palindrome, factors)

def smallest(max_factor, min_factor = 0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    return analitics(max_factor + 1, min_factor, 1)

def largest(max_factor, min_factor = 0):
    if min_factor > max_factor:
        raise ValueError("min must be <= max")
    return analitics(min_factor - 1, max_factor, -1)