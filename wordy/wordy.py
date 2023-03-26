def clean(question):
    question = question[:-1].split()
    question_clean = []

    for item in question:
        if item == "cubed":
            raise ValueError("unknown operation")
        if item.isnumeric() or item[0] == "-" and item[1:].isnumeric():
            question_clean.append(int(item))
        if item in ("plus", "minus", "divided", "multiplied"):
            question_clean.append(item.replace("plus", "+").replace("minus", "-").replace("divided", "/").replace("multiplied", "*"))

    if len(question_clean) == 0 and question[0] == "What":
        raise ValueError("syntax error")
    elif question[0] != "What":
        raise ValueError("unknown operation") 
    for i in range(1, len(question_clean)):
        if len(question_clean) == 2 and type(question_clean[i-1]) != type(question_clean[i]) or type(question_clean[i-1]) == type(question_clean[i]):
            raise ValueError("syntax error")
    return question_clean

def answer(question):
    question_clean = clean(question)
    for i in range(int((len(question_clean)-1)/2)):
        if question_clean[1] == "*":
            new_item = int(question_clean[0]) * int(question_clean[2])
            question_clean = question_clean[3:]
            question_clean.insert(0, int(new_item))
        elif question_clean[1] == "/":
            new_item = int(question_clean[0]) / int(question_clean[2])
            question_clean = question_clean[3:]
            question_clean.insert(0, int(new_item))
        elif question_clean[1] == "+":
            new_item = int(question_clean[0]) + int(question_clean[2])
            question_clean = question_clean[3:]
            question_clean.insert(0, int(new_item))
        elif question_clean[1] == "-":
            new_item = int(question_clean[0]) - int(question_clean[2])
            question_clean = question_clean[3:]
            question_clean.insert(0, int(new_item))
    return int(question_clean[0])