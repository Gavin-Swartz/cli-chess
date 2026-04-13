class Piece:
    def __init__(self, x: int, y: int, captured: bool = False):
        self.x = x
        self.y = y
        self.captured = captured
        self.moves_made: int = 0
        self.possible_moves: list[list[int]] = []       # All possible moves by piece, given as absolute board coordinates

    def update_valid_moves(self, player, opponent):
        self.possible_moves = []

    # Move piece to provided square index
    def move(self, x: int, y: int):
        self.x = x
        self.y = y
        self.moves_made += 1
