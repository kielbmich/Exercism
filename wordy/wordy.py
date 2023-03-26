#glennj's is the author of the 99% of the solution below
import re, operator

operations = {'plus': operator.add,
    'minus': operator.sub,
    'multiplied by': operator.mul,
    'divided by': operator.floordiv}

def get_number(question):
    m = re.match(r"-?\d+", question)
    if not m:
        raise ValueError("syntax error")
    return [question.removeprefix(m.group()).lstrip(), int(m.group())]

def get_operation(question):
    m = re.match(r"plus|minus|multiplied by|divided by" ,question)
    if not m:
        raise ValueError("unknown operation")
    return [question.removeprefix(m.group()).lstrip(), operations[m.group(0)]]

def prepare_question(question):
    q = question.lower().strip().removesuffix("?")
    prefix = "what is"
    if not q.startswith(prefix):
        raise ValueError("unknown operation")
    return q.removeprefix(prefix).lstrip()

def answer(question):
    q = prepare_question(question)
    q, result = get_number(q)
    while len(q) > 0:
        if re.match(r"-?\d+", q):
            raise ValueError("syntax error")
        q, operation = get_operation(q)
        q, num = get_number(q)
        result = operation(result, num)
    return result