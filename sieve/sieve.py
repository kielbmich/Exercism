def primes(limit: int) -> list:
    candidates = [*range(limit + 1)]
    for i in range(2, int(len(candidates) ** (1/2) + 1)):
        if candidates[i]:
            for j in range(i*i, limit + 1, i):
                candidates[j] = False
    return [i for i in candidates if i][1:]