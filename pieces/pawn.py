from board import get_piece_at_square, on_board
from turn_utils import get_previously_moved_piece
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
        if len(self.possible_moves) != 0 and not self.moves_made:
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

        # En passant for either direction
        newY = self.y
        for newX in [self.x-1, self.x+1]:
            if on_board(newX, newY):
                # TODO check if opponent piece moved two spaces
                # Check if opponent piece exists, is a pawn, has only moved once, and was the most recently moved piece
                opponent_piece = get_piece_at_square(opponent.pieces, newX, newY)
                
                print(not opponent_piece.captured)
                print(type(opponent_piece) is Pawn)
                print(opponent_piece is get_previously_moved_piece())
                print(opponent_piece.moves_made == 1)

                if (not opponent_piece.captured) and (type(opponent_piece) is Pawn) and (opponent_piece is get_previously_moved_piece()) and (opponent_piece.moves_made == 1):
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
