def append(list1, list2):
    return list1 + list2


def concat(lists): 
    return [item for sublist in lists for item in sublist]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    out = 0
    for item in list:
        out += 1
    return out


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for item in list[::-1]:
        accumulator = function(item, accumulator)
    return accumulator 


def reverse(list):
    return list[::-1]