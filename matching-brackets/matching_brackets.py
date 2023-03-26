pairs = {"(" : ")", "[" : "]", "{" : "}"}

def is_paired(input_string):
    stack = []
    for c in input_string:
        if c in pairs.keys():
            stack.append(c)
        elif c in pairs.values():
            if not stack or pairs[stack.pop()] != c:
                return False
    return not stack

import cProfile
def main():
    is_paired("D#{}[a-ds{ł(})[}"*100000)

if __name__ == '__main__':
    cProfile.run('main()')

# ...     cProfile.run('main()')
# ... 
#          33 function calls in 0.001 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <stdin>:1(is_paired)
#         1    0.001    0.001    0.001    0.001 <stdin>:1(main)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
#         2    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
#         9    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
