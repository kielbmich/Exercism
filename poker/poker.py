def best_hands(hands):
    pass

import re
five_of_kind = re.compile(r"(A[C|D|H|S]){4}")

x = five_of_kind.search("KS AH AS AD AC")
x
print(x)
