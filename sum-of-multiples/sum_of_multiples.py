def sum_of_multiples(limit, multiples):
    my_set = set()
    if 0 in multiples:
        multiples.remove(0)
    for item in multiples:
            my_set.update(range(item, limit, item))
    return sum(my_set)