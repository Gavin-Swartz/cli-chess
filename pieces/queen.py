from pieces.piece import Piece


class Queen(Piece):
    rep = 'Q'
    name = 'queen'

    def update_valid_moves(self, player, opponent):
        return super().update_valid_moves(player, opponent)