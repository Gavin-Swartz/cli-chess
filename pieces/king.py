from pieces.piece import Piece
from board import get_piece_at_square, on_board


class King(Piece):
    rep = 'K'
    name = 'king'

    def update_valid_moves(self, player, opponent):
        # Reset possible moves
        self.possible_moves = []

        # Captured pieces have no possible moves
        if self.captured:
            return
        
        # Check for valid moves in all 8 potential squares
        for dY in [-1, 0, 1]:
            for dX in [-1, 0, 1]:
                newX = self.x + dX
                newY = self.y + dY

                if on_board(newX, newY):
                    if get_piece_at_square(player.pieces, newX, newY).captured:
                        self.possible_moves.append([newX, newY])