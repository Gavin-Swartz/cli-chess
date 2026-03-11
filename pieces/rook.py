from board import get_piece_at_square, on_board
from pieces.piece import Piece


class Rook(Piece):
    rep = 'R'
    name = 'rook'

    def _validate_rook_squares(self, player, opponent, x, y):
        # Ensure no piece from same player on square
        if not get_piece_at_square(player.pieces, x, y).captured:
            return False
        # Ensure square is on board
        elif not on_board(x, y):
            return False
        # If opponent piece at square, square is valid move but discontinue search in direction
        elif not get_piece_at_square(opponent.pieces, x, y).captured:
            self.possible_moves.append([x, y])
            return False
        # If empty square, move is valid
        else:
            self.possible_moves.append([x, y])
            return True


    def update_valid_moves(self, player, opponent):
        # Reset possible moves
        self.possible_moves = []

        # Captured pieces have no possible moves
        if self.captured:
            return
        
        # Search in both positive and negative directions
        for direction in [-1, 1]:
            # Get all moves in row
            searching = True
            newX = self.x
            while searching:
                newX += direction   # Iterate positively or negatively
                searching = self._validate_rook_squares(player, opponent, newX, self.y)

            # Get all moves in column
            searching = True
            newY = self.y
            while searching:
                newY += direction
                searching = self._validate_rook_squares(player, opponent, self.x, newY)
