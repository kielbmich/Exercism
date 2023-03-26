def is_palindrome(number):
    return True if str(number) == str(number)[::-1] else False

def better_than_previous(i, j, palindrome, order):
    if palindrome == None:
        return False 
    return True if (order == 1 and i*j < palindrome) or (order == -1 and i*j > palindrome) else False

def best_possible_palindrome(i, palindrome, order):
    if palindrome == None:
        return False 
    return True if (order == 1 and i*i > palindrome) or (order == -1 and i*i < palindrome) else False

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
                if better_than_previous(i, j, palindrome, order):
                    palindrome = i*j
                    factors = [[i,j]]
        if best_possible_palindrome(i, palindrome, order):
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