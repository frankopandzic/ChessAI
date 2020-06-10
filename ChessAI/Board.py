from Square import Square
from Pieces import Pawn, Knight, Bishop, Rook, Queen, King


class Board:
    def __init__(self):
        self.board = [[0 for j in range(8)] for i in range(8)]
        self.white_pieces = []
        self.black_pieces = []
        # making a chess board with 8x8(64) total squares
        for index in range(1,9):
            for letter in range(1,9):
                self.board[index-1][letter-1] = Square((letter, index))
                # making a board with black and white chess pieces
                if index == 1:
                    if letter in [1, 8]:
                        self.board[index-1][letter - 1].set_figure(Rook(True, (letter, index)))
                        self.white_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter in [2, 7]:
                        self.board[index-1][letter - 1].set_figure(Knight(True, (letter, index)))
                        self.white_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter in [3, 6]:
                        self.board[index-1][letter - 1].set_figure(Bishop(True, (letter, index)))
                        self.white_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter == 4:
                        self.board[index-1][letter - 1].set_figure(Queen(True, (letter, index)))
                        self.white_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter == 5:
                        self.board[index-1][letter - 1].set_figure(King(True, (letter, index)))
                        self.white_pieces.append(self.board[index-1][letter - 1].get_figure())
                elif index == 8:
                    if letter in [1, 8]:
                        self.board[index-1][letter - 1].set_figure(Rook(False, (letter, index)))
                        self.black_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter in [2, 7]:
                        self.board[index-1][letter - 1].set_figure(Knight(False, (letter, index)))
                        self.black_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter in [3, 6]:
                        self.board[index-1][letter - 1].set_figure(Bishop(False, (letter, index)))
                        self.black_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter == 4:
                        self.board[index-1][letter - 1].set_figure(Queen(False, (letter, index)))
                        self.black_pieces.append(self.board[index-1][letter - 1].get_figure())
                    elif letter == 5:
                        self.board[index-1][letter - 1].set_figure(King(False, (letter, index)))
                        self.black_pieces.append(self.board[index-1][letter - 1].get_figure())
                elif index == 2:
                    self.board[index-1][letter-1].set_figure(Pawn(True, (letter, index)))
                    self.white_pieces.append(self.board[index-1][letter - 1].get_figure())
                elif index == 7:
                    self.board[index-1][letter - 1].set_figure(Pawn(False, (letter, index)))
                    self.black_pieces.append(self.board[index-1][letter - 1].get_figure())

    # updates positions of chess pieces on the chessboard
    # this function is called only if legal_move() returns True for the same start and destination values
    def update_board(self, start, destination):
        # start and destination are tuples containing coordinates on the chessboard
        s_letter = start[0]-1
        s_index = start[1]-1
        d_letter = destination[0]-1
        d_index = destination[1]-1

        # remove piece from start coordinates
        figure = self.board[s_letter][s_index].get_figure()
        self.board[s_letter][s_index].set_figure(None)
        self.board[s_letter][s_index].set_occupation(False)

        # move piece to destination coordinates
        self.board[d_letter][d_index].set_figure(figure)
        if not self.board[d_letter][d_index].is_occupated():
            self.board[d_letter][d_index].set_occupation(True)

    def legal_move(self, start, destination):
        # start and destination are tuples containing position on the chessboard
        pass

    def get_white_pieces(self):
        return self.white_pieces

    def get_black_pieces(self):
        return self.black_pieces

    def get_board(self):
        return self.board

    def print_board(self):
        temp_board = self.board.copy()
        temp_board.reverse()
        for row in temp_board:
            s_row = ""
            for square in row:
                if square.is_occupated():
                    figure = square.get_figure()
                    name = figure.get_name()
                    if name == "Knight":
                        if figure.get_color() == "Black":
                            s_row += "♞  "
                        else:
                            s_row += "♘  "
                    elif name == "Rook":
                        if figure.get_color() == "Black":
                            s_row += "♜  "
                        else:
                            s_row += "♖  "
                    elif name == "Pawn":
                        if figure.get_color() == "Black":
                            s_row += "♟  "
                        else:
                            s_row += "♙  "
                    elif name == "Queen":
                        if figure.get_color() == "Black":
                            s_row += "♛  "
                        else:
                            s_row += "♕  "
                    elif name == "Bishop":
                        if figure.get_color() == "Black":
                            s_row += "♝  "
                        else:
                            s_row += "♗  "
                    elif name == "King":
                        if figure.get_color() == "Black":
                            s_row += "♚  "
                        else:
                            s_row += "♔  "
                else:
                    s_row += "   "
            print(s_row)
