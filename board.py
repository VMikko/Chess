import pieces

class Square:
    def __init__(self,):
        self.color: int = None #0 is black, 1 is white
        self._piece: pieces.Piece = None
        self.coord: tuple[int, int] = None # To be defined when initializing the board
        self.string: str = None # To be used when setting the colour of the square

    def setSquareBlack(self):
        self.color = 0
        self.string = "■"
    def setSquareWhite(self):
        self.color = 1
        self.string = "□"
    
    def __str__(self) -> str:
        if self._piece:
            return f'{self.piece}'
        else:
            return self.string

    def isEmpty(self) -> bool:
        return not (self.piece)

    def getPiece(self) -> pieces.Piece:
        return self._piece

    def setPiece(self, p: pieces.Piece):
        self._piece = p

    def removePiece(self):
        self._piece = None

    piece = property(getPiece, setPiece)

#Board consists of a 8x8 matrix full of Squares
class Chessboard:
    whitePieces: list[pieces.Piece] = []
    blackPieces: list[pieces.Piece] = []
    whiteKing: pieces.Piece = None
    blackKing: pieces.Piece = None
    deadPieces: list[pieces.Piece] = []

    def __init__(self) -> None:
        #Initializes the board full of empty squares (with proper colors)
        self.board = [[Square() for _ in range(8)] for _ in range(8)]
        for i in range(8):
            for j in range(8):
                if (j+i) % 2 == 0:
                    self.board[i][j].setSquareWhite()
                    self.board[i][j].coord = [j, i]
                else:
                    self.board[i][j].setSquareBlack()
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
        return self.selectSquare(coord).getPiece()


    def killPiece(self, coord: tuple[int, int]):
        """Kills the piece in the given coordinate, adding it to the deadPieces list
        
        To be used when another piece moves into the coord
        
        Does not check if the capture is legal (can capture your own pieces)
        """
        if not (self.selectSquare(coord).isEmpty()):
            piece = self.selectPiece(coord)
            self.deadPieces.append(piece)
            self.removePiece(coord)
            if (piece.color):
                self.whitePieces.remove(piece)
            else:
                self.blackPieces.remove(piece)    
            del piece # TODO: is this necessary?  
    
    def removePiece(self, coord: tuple[int, int]): #I should rename this to like emptySquare
        """Sets the piece in the given coordinates to None, to be used when moving or capturing a piece
        """
        self.selectSquare(coord).removePiece()

    def movePiece(self, origCoord: tuple[int, int], targetCoord: tuple[int, int]):
        """Moves the piece from original coord to target coord
        """
        self.killPiece(targetCoord) ## Should I remove this?
        #Does this work?
        self.selectSquare(targetCoord).piece = self.selectPiece(origCoord)
        self.selectPiece(targetCoord).updateLocation(targetCoord)
        self.removePiece(origCoord)


    def addPiece(self, p: pieces.Piece, coord: tuple[int, int], color = 1):
        """Adds a piece to the given coordinate

        color is assumed to be white if not specified (0 is black, 1 is white)

        Checks if the given square is empty or not
        """
        if self.selectSquare(coord).isEmpty():
            self.selectSquare(coord).setPiece(p(coord))
            self.selectPiece(coord).setColor(color)
            #self.selectPiece(coord).color = color
            if color == 0:
                self.blackPieces.append(self.selectPiece(coord))
            else:
                self.whitePieces.append(self.selectPiece(coord))
                
            
        
        

    def setBoard(self):
        #Pawns
        for y in (1, 6):
            for x in range(8):
                if (y == 1):
                    self.addPiece(pieces.Pawn, [x,y], 0)
                else:
                    self.addPiece(pieces.Pawn, [x,y], 1)
                    
        #Other stuff
        
        for y in (0, 7):
            #Rooks
            for x in (0, 7):
                self.addPiece(pieces.Rook, [x,y], y)
            #Knights
            for x in (1, 6):
                self.addPiece(pieces.Knight, [x,y], y)
            #Bishops
            for x in (2, 5):
                self.addPiece(pieces.Bishop, [x,y], y)

        # Queens
        self.addPiece(pieces.Queen, [4,0], 0)

        self.addPiece(pieces.Queen, [3,7], 1)
        #Kings
        self.addPiece(pieces.King, [3,0], 0)
        self.blackKing = self.selectPiece([3,0])
        self.addPiece(pieces.King, [4,7], 1)
        self.whiteKing = self.selectPiece([4,7])