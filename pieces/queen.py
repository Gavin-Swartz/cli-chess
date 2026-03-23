from pieces.piece import Piece
from pieces.piece_utils import validate_rook_bishop_squares


class Queen(Piece):
    rep = 'Q'
    name = 'queen'
    available_directions = [[1, 1], [-1, 1], [1, -1], [-1, -1], [0, 1], [0, -1], [1, 0], [-1, 0]]

    def update_valid_moves(self, player, opponent):
        # Reset possible moves
        self.possible_moves = []

        # Captured pieces have no possible moves
        if self.captured:
            return
        
        # Search in all 4 diagonals and all 4 directions
        for direction in self.available_directions:
            newX = self.x
            newY = self.y

            searching = True
            while searching:
                newX += direction[0]
                newY += direction[1]

                searching = validate_rook_bishop_squares(player, opponent, newX, newY, self)
