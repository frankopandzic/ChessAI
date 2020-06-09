from Square import Square
from Pieces import Pawn, Knight, Bishop, Rook, Queen, King


class Board:
    def __init__(self):
        self.board = [[0 for j in range(8)] for i in range(8)]
        self.white_pieces = []
        self.black_pieces = []
        cnt = 0
        for index in range(1,9):
            for letter in range(1,9):
                self.board[cnt][letter-1] = Square((letter, index))
                # making a board with black and white chess pieces
                if index == 1:
                    if letter in [1, 8]:
                        self.board[cnt][letter - 1].set_figure(Rook(True, (letter, index)))
                        self.white_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter in [2, 7]:
                        self.board[cnt][letter - 1].set_figure(Knight(True, (letter, index)))
                        self.white_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter in [3, 6]:
                        self.board[cnt][letter - 1].set_figure(Bishop(True, (letter, index)))
                        self.white_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter == 4:
                        self.board[cnt][letter - 1].set_figure(Queen(True, (letter, index)))
                        self.white_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter == 5:
                        self.board[cnt][letter - 1].set_figure(King(True, (letter, index)))
                        self.white_pieces.append(self.board[cnt][letter - 1].get_figure())
                elif index == 8:
                    if letter in [1, 8]:
                        self.board[cnt][letter - 1].set_figure(Rook(False, (letter, index)))
                        self.black_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter in [2, 7]:
                        self.board[cnt][letter - 1].set_figure(Knight(False, (letter, index)))
                        self.black_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter in [3, 6]:
                        self.board[cnt][letter - 1].set_figure(Bishop(False, (letter, index)))
                        self.black_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter == 4:
                        self.board[cnt][letter - 1].set_figure(Queen(False, (letter, index)))
                        self.black_pieces.append(self.board[cnt][letter - 1].get_figure())
                    elif letter == 5:
                        self.board[cnt][letter - 1].set_figure(King(False, (letter, index)))
                        self.black_pieces.append(self.board[cnt][letter - 1].get_figure())
                elif index == 2:
                    self.board[cnt][letter-1].set_figure(Pawn(True, (letter, index)))
                    self.white_pieces.append(self.board[cnt][letter - 1].get_figure())
                elif index == 7:
                    self.board[cnt][letter - 1].set_figure(Pawn(False, (letter, index)))
                    self.black_pieces.append(self.board[cnt][letter - 1].get_figure())
            cnt += 1
        print(self.white_pieces)
        print(self.black_pieces)

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces

    def get_board(self):
        return self.board
