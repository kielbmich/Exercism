def transpose(lines):
    lines = lines.split("\n")
    cols = len(max(lines, key=len)) if lines else 1
    out = ["" for col in range(cols)]
    for index in range(cols):
        for item in lines:
            try:
                out[index] += item[index]
            except IndexError:
                out[index] += "@"
    for index in range(len(out)):
        out[index] = out[index].rstrip("@").replace("@", " ")
    return "\n".join(out)