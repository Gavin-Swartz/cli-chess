from board import get_piece_at_square, on_board
from pieces.piece import Piece


class Knight(Piece):
    rep = 'N'
    name = 'knight'

    # All moves the piece can make, disregarding board bounds and other pieces
    moves = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]

    def update_valid_moves(self, player, opponent):
        # Reset list of possible moves
        self.possible_moves = []

        # Captured pieces have cannot move
        if self.captured:
            return
        
        # Iterate over moves piece could make
        for move in self.moves:
            newX = self.x + move[0]
            newY = self.y + move[1]

            # Check if space is on the board and no piece from same player on space
            if on_board(newX, newY) and get_piece_at_square(player.pieces, newX, newY).captured:
                self.possible_moves.append([newX, newY])
