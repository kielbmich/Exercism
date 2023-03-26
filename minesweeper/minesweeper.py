def board(minefield):
    for row in minefield:
        valid = True if len(row) == len(minefield[0]) else False
        if not valid:
            return False
        for item in row:
            valid = True if item in " *" else False
            if not valid:
                return False
    return True

def annotate(minefield):
    if not board(minefield):
        raise ValueError("The board is invalid with current input.")
    out = []
    for i in range(len(minefield)):
        current_row = ""
        for j in range(len(minefield[i])):
            mines_neighbour = ""
            for n in range(-1, 2):
                for m in range(-1, 2):
                    if(i + n >= 0 and j + m >= 0):
                        try:
                            mines_neighbour += str(minefield[i+n][j+m])
                        except IndexError:
                            pass
            mines_neighbour = mines_neighbour.count("*")
            if minefield[i][j] == " ":
                current_row += str(mines_neighbour) if mines_neighbour > 0 else " "
            if minefield[i][j] == "*":
                current_row += "*"
        out.append(current_row)
    return out