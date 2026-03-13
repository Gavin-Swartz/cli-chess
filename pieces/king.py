from pieces.piece import Piece


class King(Piece):
    rep = 'K'
    name = 'king'

    def update_valid_moves(self, player, opponent):
        return super().update_valid_moves(player, opponent)