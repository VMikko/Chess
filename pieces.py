from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, coord: list[int, int]) -> None:
        self._color: int = 1
        self._coord: list[int, int] = coord

    def getColor(self) -> int:
        return self._color
    

    def setColor(self, color = 1):
        """If color is anything but 0, set it white (1)
        Else if its 0, set it to black (0)"""
        if color == 0:
            self._color = 0
        else:
            self._color = 1
    
    def location(self) -> tuple[int]:
        return self._coord

    def updateLocation(self, coord: tuple[int]):
        self._coord = coord

    def __str__(self):
        f'{self.getColor()} at {self.location()}'

    color = property(getColor, setColor)
    coord = property(location, updateLocation)
    

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
            return "N"
        else:
            return "n"

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
            return "K"
        else:
            return "k"
        
        