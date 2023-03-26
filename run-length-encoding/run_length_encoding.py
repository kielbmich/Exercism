from itertools import groupby
import re

def decode(string):
    out = []
    string_grouped = re.findall(r"(\d*)(.)", string)
    for decode_pair in string_grouped:
        if decode_pair[0]:
            out.append(f"{int(decode_pair[0]) * decode_pair[1]}")
        else:
            out.append(decode_pair[1])
    return "".join(out)

def encode(string):
    out = []
    for chr, occ in groupby(string):
        occurences = len(list(occ))
        if occurences == 1:
            out.append(chr)
        else:
            out.append(f"{occurences}{chr}")
    return "".join(out)