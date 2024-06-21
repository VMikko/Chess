import board

# A singular chessgame
# goes turn by turn, tracks rounds etc etc.
class ChessGame:
    gameboard = board.Chessboard()
    round: int = 0
    def __init__(self):
        self.gameboard.setBoard()
        self.gameboard.printBoard()        
        
    ##TODO: if an error happens, tell of it (for example, trying to move your own piece on top of another own piece) and reset the turn
    def error():
        pass
