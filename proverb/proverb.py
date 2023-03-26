saying = [
    "For want of a {} the {} was lost.",
    "And all for the want of a {}."
]

def proverb(*inputs, qualifier = None):
    out = [saying[0].format(a, b) for a, b in zip(inputs[:-1], inputs[1:])]
    if inputs:
        out.append(saying[1].format(qualifier + " " + inputs[0]) if qualifier else saying[1].format(inputs[0]))
    return out
