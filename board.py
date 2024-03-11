class Square:
    def __init__(self):
        self.color = 1
        self.piece = ""

    def setBlack(self):
        self.color = 0
    
    def setWhite(self):
        self.color = 1

    def __str__(self) -> str:
        if self.piece == "":
            return str(self.color)
        else:
            return str(self.piece)


#Board consists of a 8x8 matrix full of Squares
class Chessboard:
    def __init__(self) -> None:
        self.board = [[Square() for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if (j+i) % 2 == 0:
                    self.board[i][j].setWhite()
                else:
                    self.board[i][j].setBlack()
                    
    def printBoard(self):
        for i in range(8):
            print(str(8-i) + "|", end= " ")
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()
        print("  ________________")
        print("   A B C D E F G H")
