from board import get_piece_at_square, on_board
from pieces.piece import Piece


class Pawn(Piece):
    rep = 'p'
    # potential_moves = [[0, 1], [0, 2], [-1, 1], [1, 1]]     # Potential moves relative to piece's current location


    def update_valid_moves(self, player, opponent):
        # Reset possible moves
        self.possible_moves = []

        # Captured pieces have no possible moves
        if self.captured:
            return
        
        # Get piece orientation based on player
        orient = 1
        if player.color == 'w':
            orient = -1

        # Forward 1 squares
        newX = self.x
        newY = self.y + (1 * orient)
        if on_board(newX, newY):
            if get_piece_at_square(opponent.pieces, newX, newY).captured and get_piece_at_square(player.pieces, newX, newY).captured:
                self.possible_moves.append([newX, newY])

        # Forward 2 squares (path cannot be blocked and must be first move by piece)
        if len(self.possible_moves) != 0 and self.unmoved:
            newX = self.x
            newY = self.y + (2 * orient)
            if get_piece_at_square(opponent.pieces, newX, newY).captured and get_piece_at_square(player.pieces, newX, newY).captured:
                self.possible_moves.append([newX, newY])

        # Diagonal left (relative to white player at bottom)
        newX = self.x + 1
        newY = self.y + (1 * orient)
        if on_board(newX, newY):
            # Move is valid if an opposing piece is present at diagonal
            if not get_piece_at_square(opponent.pieces, newX, newY).captured:
                self.possible_moves.append([newX, newY])

        # Diagonal right (relative to white player at bottom)
        newX = self.x - 1
        newY = self.y + (1 * orient)
        if on_board(newX, newY):
            # Move is valid if an opposing piece is present at diagonal
            if not get_piece_at_square(opponent.pieces, newX, newY).captured:
                self.possible_moves.append([newX, newY])
