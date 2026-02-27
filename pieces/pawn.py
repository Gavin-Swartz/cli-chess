from pieces.piece import Piece


class Pawn(Piece):
    rep = 'p'

    def valid_move(self, oX, oY, tX, tY, player):
        # Get possible number of rows that can be progressed
        possible_forward_moves = []
        if self.unmoved:
            possible_forward_moves = [1, 2]
        else:
            possible_forward_moves = [1]

        # Get piece orientation based on player
        if player == 'w':
            possible_forward_moves = [-move for move in possible_forward_moves]
        
        # Check if move is possible
        row_distance = tY - oY
        if (oX == tX) and (row_distance in possible_forward_moves):
            return True
        else:
            return False