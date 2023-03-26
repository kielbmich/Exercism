def flatten(iterable):
    out = []
    for x in iterable:
        if isinstance(x, list):
            out.extend(flatten(x))
        elif x is not None:
            out.append(x)
    return out
