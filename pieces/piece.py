class Piece:
    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def move(self, newX, newY):
        self.posX = newX
        self.posY = newY
