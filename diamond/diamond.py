def rows(letter):
    diff = ord(letter) - ord("A")
    letters = [chr(ord) for ord in range(65, ord(letter)+1)]
    partial_diamond = []
    for index, item in enumerate(letters):
        current_row = [item if i in (diff-index, diff+index) else " " for i in range(diff*2+1)]
        partial_diamond.append("".join(current_row))
    return partial_diamond[:-1] + partial_diamond[::-1]