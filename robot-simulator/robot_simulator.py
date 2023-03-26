# Globals for the directions
# Change the values as you see fit
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
DIRECTIONS = {NORTH: (0, 1), EAST: (1, 0), SOUTH: (0, -1), WEST: (-1, 0)}


class Robot:

    def __init__(self, direction: int = NORTH, x_pos: int = 0, y_pos: int = 0) -> None:
        self.coordinates = (x_pos, y_pos)
        self.direction = direction

    def turn(self, turn: int) -> None:
        make_turn = -1 if turn == "L" else 1
        self.direction = (self.direction + make_turn) % 4

    def advance(self) -> None:
        self.coordinates = tuple(i + j for i, j in zip(self.coordinates, DIRECTIONS[self.direction]))

    def move(self, moves: str) -> tuple[int, int]:
        for move in moves:
            if move in "LR":
                self.turn(move)
            elif move == "A":
                self.advance()
        return self.coordinates