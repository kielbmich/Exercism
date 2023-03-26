def triplets_with_sum(number):
    out = []
    for a in range(1, number//3):
        for b in range(max(a + 1, number//2 - a), (number - a)//2 + 1):
            ab = a * a + b * b
            c = number - a - b
            if ab == c * c:
                out.append([a, b, c])
    return out