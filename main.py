import board


def main():
    gameboard = board.Chessboard()
    gameboard.setBoard()
    gameboard.printBoard()
    print(gameboard.blackKingLocation)
    

if __name__ == "__main__":
    main()