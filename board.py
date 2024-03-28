import pieces

class Square:
    def __init__(self,):
        self.color: int = 1
        self.piece: pieces.Piece = pieces.Empty
        self.coord: tuple[int, int] = None

    def setBlack(self):
        self.color = 0
    
    def setWhite(self):
        self.color = 1
    
    def __str__(self) -> str:
        if self.piece == pieces.Empty:
            if self.color == 1:
                return "□"
            else:
                return "■"
        else:
            return f"{self.piece}"

#Board consists of a 8x8 matrix full of Squares
class Chessboard:
    whitePieces: list[pieces.Piece] = []
    blackPieces: list[pieces.Piece] = []
    whiteKingLocation: list[int] = []
    blackKingLocation: list[int] = []

    def __init__(self) -> None:
        #Initializes the board full of empty squares (with proper colors)
        self.board = [[Square() for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if (j+i) % 2 == 0:
                    self.board[i][j].setWhite()
                    self.board[i][j].coord = [j, i]
                else:
                    self.board[i][j].setBlack()
                    self.board[i][j].coord = [j, i]
            

    def printBoard(self):
        for i in range(8):
            print(str(8-i) + "|", end= " ")
            for j in range(8):
                print(self.board[i][j], end=" ")
            print()
        print("  ________________")
        print("   A B C D E F G H")
    

    def selectSquare(self, coord: tuple[int, int]) -> Square:
        return self.board[coord[1]][coord[0]]

    def selectPiece(self, coord: tuple[int, int]) -> pieces.Piece:
        return self.board[coord[1]][coord[0]].piece
        #return self.selectSquare(coord).piece
    

        

    def setBoard(self):
        #Pawns
        for y in (1, 6):
            for x in range(8):
                #Testing stuff, didnt work
                #piece = self.selectSquare([x,y]).piece
                self.board[y][x].piece = pieces.Pawn((x, y))
                if (y == 1):
                    #self.board[y][x].piece.setBlack()
                    #piece.setBlack()
                    #self.selectSquare([x,y]).piece.setBlack()
                    self.selectPiece([x,y]).setBlack()
                    self.blackPieces.append(self.selectPiece([x,y]))
                else:
                    self.whitePieces.append((self.selectPiece([x,y])))
        
        #Other stuff
        for y in (0, 7):
            #Rooks
            for x in (0, 7):
                self.board[y][x].piece = pieces.Rook((x,y))
                if (y == 0):
                    self.selectPiece([x,y]).setBlack()
                    self.blackPieces.append(self.selectPiece([x,y]))
                else:
                    self.whitePieces.append(self.selectPiece([x,y]))
            #Knights
            for x in (1, 6):
                self.board[y][x].piece = pieces.Knight((x,y))
                if (y == 0):
                    self.selectPiece([x,y]).setBlack()
                    self.blackPieces.append(self.selectPiece([x,y]))
                else:
                    self.whitePieces.append(self.selectPiece([x,y]))
            #Bishops
            for x in (2, 5):
                self.board[y][x].piece = pieces.Bishop((x,y))
                if (y == 0):
                    self.selectPiece([x,y]).setBlack()
                    self.blackPieces.append(self.selectPiece([x,y]))
                else:
                    self.whitePieces.append(self.selectPiece([x,y]))

        # Queens
        self.board[0][4].piece = pieces.Queen((0,4))
        self.selectPiece([4,0]).setBlack()
        self.blackPieces.append(self.selectPiece([4,0]))
        self.board[7][3].piece = pieces.Queen((7,3))
        self.whitePieces.append(self.selectPiece([3,7]))
        #Kings
        self.board[0][3].piece = pieces.King((0,3))
        self.board[0][3].piece.setBlack()
        self.blackPieces.append(self.selectPiece([3,0]))
        #This should always update automatically as the king moves, I hope.
        self.blackKingLocation = self.selectPiece([3,0]).coord
        self.board[7][4].piece = pieces.King((7,4))
        self.whitePieces.append(self.selectPiece([4,0]))
        self.whiteKingLocation = self.selectPiece([4,7]).coord
        #TODO: Make sure the kings' locations always update when they get moved