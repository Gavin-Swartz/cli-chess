from board import get_piece_at_square, on_board
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.piece import Piece
from pieces.queen import Queen
from pieces.rook import Rook


class Pawn(Piece):
    rep = 'p'
    name = 'pawn'

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


    def promote_pawn(self, player):
        # Get pawn coordinates
        x = self.x
        y = self.y

        valid = False
        while not valid:
            # Get user input
            user_selection = input(f"({player.color}) Pawn ready for promotion. Enter piece type (N, B, R, Q): ")
            user_selection = str(user_selection).upper()

            # Create new piece
            if user_selection == 'N':
                player.pieces.append(Knight(x, y))
                valid = True
            elif user_selection == 'B':
                player.pieces.append(Bishop(x, y))
                valid = True
            elif user_selection == 'R':
                player.pieces.append(Rook(x, y))
                valid = True
            elif user_selection == 'Q':
                player.pieces.append(Queen(x, y))
                valid = True
            else:
                'Invalid piece. Try again.'

        # Capture to remove pawn
        self.captured = True
