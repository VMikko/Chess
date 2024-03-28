from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, coord: list[int, int]) -> None:
        self.color = 1
        self.coord = coord

    def setWhite(self):
        self.color = 1
    def setBlack(self):
        self.color = 0

    #This doesn't work?
    def location(self) -> list[int]:
        return self.coord

    #@abstractmethod
    #def possibleMoves(self):
     #   pass
    

class Pawn(Piece):
    def __str__(self):
        if self.color == 1:
            return "P"
        else:
            return "p"
        
class Empty(Piece):
    def __init__(self):
        self.color = 1


    def __str__(self):
        return "empty"


class Rook(Piece):
    def __str__(self):
        if self.color == 1:
            return "R"
        else:
            return "r"

class Knight(Piece):
    def __str__(self):
        if self.color == 1:
            return "K"
        else:
            return "k"

class Bishop(Piece):
    def __str__(self):
        if self.color == 1:
            return "B"
        else:
            return "b"

class Queen(Piece):
    def __str__(self):
        if self.color == 1:
            return "Q"
        else:
            return "q"

class King(Piece):
    def __str__(self):
        if self.color ==1:
            return "G"
        else:
            return "g"
        
        