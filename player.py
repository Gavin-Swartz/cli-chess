from pieces.piece import Piece


class Player():
    def __init__(self, color_char: str):
        self.color = color_char
        self.pieces : Piece = []
