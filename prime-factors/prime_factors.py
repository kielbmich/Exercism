def factors(value):
    dividors = []
    while value > 1:
        for divisor in range(2, value + 1):
            if value % divisor == 0:
                dividors.append(divisor)
                value = int(value/divisor)
                break
    return dividors