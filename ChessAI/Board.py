import Square
from Pieces import Pawn, Knight, Bishop, Rook, Queen, King

class Board:
    def __init__(self):
        board = [[0 for j in range(8)] for i in range(8)]
        cnt = 0
        for index in range(1,9):
            for letter in range(1,9):
                board[cnt][letter-1] = Square((letter, index))
                # making a board with black and white chess pieces
                if index == 1:
                    if letter in [1, 8]:
                        board[cnt][letter - 1].set_figure(Rook(True, (letter, index)))
                    elif letter in [2, 7]:
                        board[cnt][letter - 1].set_figure(Knight(True, (letter, index)))
                    elif letter in [3, 6]:
                        board[cnt][letter - 1].set_figure(Bishop(True, (letter, index)))
                    elif letter == 4:
                        board[cnt][letter - 1].set_figure(Queen(True, (letter, index)))
                    elif letter == 5:
                        board[cnt][letter - 1].set_figure(King(True, (letter, index)))
                elif index == 8:
                    if letter in [1, 8]:
                        board[cnt][letter - 1].set_figure(Rook(False, (letter, index)))
                    elif letter in [2, 7]:
                        board[cnt][letter - 1].set_figure(Knight(False, (letter, index)))
                    elif letter in [3, 6]:
                        board[cnt][letter - 1].set_figure(Bishop(False, (letter, index)))
                    elif letter == 4:
                        board[cnt][letter - 1].set_figure(Queen(False, (letter, index)))
                    elif letter == 5:
                        board[cnt][letter - 1].set_figure(King(False, (letter, index)))
                elif index == 2:
                    board[cnt][letter-1].set_figure(Pawn(True, (letter, index)))
                elif index == 7:
                    board[cnt][letter - 1].set_figure(Pawn(False, (letter, index)))
            cnt += 1
