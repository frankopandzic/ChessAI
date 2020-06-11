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
    # returns instance of Pieces.py class that needs removing after the board update, or None if no figure needs removing
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

        # if destination square is occupated, remove that figure from the game
        dead = False
        if self.board[d_letter][d_index].is_occupated():
            dead_piece = self.board[d_letter][d_index].get_figure()
            dead = True
            if dead_piece.get_color() == "Black":
                self.black_pieces.remove(dead_piece)
            else:
                self.white_pieces.remove(dead_piece)

        # move piece to destination coordinates
        self.board[d_letter][d_index].set_figure(figure)
        if not self.board[d_letter][d_index].is_occupated():
            self.board[d_letter][d_index].set_occupation(True)

        if dead:
            return dead_piece
        else:
            return None

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

    # returns all possible moves a pawn can make from his position
    def possible_pawn_moves(self, own_position, color):
        possible_moves = []
        index = own_position[0]
        letter = own_position[1]
        if color == "Black":
            if index == 7:
                if not self.board[index - 2][letter].is_occupated():
                    possible_moves.append((index - 2, letter))
            if index >= 2:
                if not self.board[index - 1][letter].is_occupated():
                    possible_moves.append((index - 1, letter))
                if self.board[index - 1][letter - 1].is_occupated() and self.board[index - 1][
                    letter - 1].get_figure().get_color() == "White":
                    possible_moves.append((index - 1, letter - 1))
                if self.board[index - 1][letter + 1].is_occupated() and self.board[index - 1][
                    letter + 1].get_figure().get_color() == "White":
                    possible_moves.append((index - 1, letter + 1))
            # check if en_passant is possible
            if self.board[index][letter - 1].is_occupated():
                figure = self.board[index][letter - 1].get_figure()
                if figure.get_name() == "Pawn" and figure.get_color == "White" and figure.get_en_passant() is True:
                    possible_moves.append((index - 1, letter - 1))
            if self.board[index][letter + 1].is_occupated():
                figure = self.board[index][letter + 1].get_figure()
                if figure.get_name() == "Pawn" and figure.get_color == "White" and figure.get_en_passant() is True:
                    possible_moves.append((index - 1, letter + 1))
        else:
            if index == 2:
                if not self.board[index + 2][letter].is_occupated():
                    possible_moves.append((index + 2, letter))
            if index <= 7:
                if not self.board[index + 1][letter].is_occupated():
                    possible_moves.append((index + 1, letter))
                if self.board[index + 1][letter + 1].is_occupated() and self.board[index + 1][
                    letter + 1].get_figure().get_color() == "White":
                    possible_moves.append((index + 1, letter + 1))
                if self.board[index + 1][letter - 1].is_occupated() and self.board[index + 1][
                    letter - 1].get_figure().get_color() == "White":
                    possible_moves.append((index + 1, letter - 1))
                # check if en_passant is possible
                if self.board[index][letter - 1].is_occupated():
                    figure = self.board[index][letter - 1].get_figure()
                    if figure.get_name() == "Pawn" and figure.get_color == "White" and figure.get_en_passant() is True:
                        possible_moves.append((index + 1, letter - 1))
                if self.board[index][letter + 1].is_occupated():
                    figure = self.board[index][letter + 1].get_figure()
                    if figure.get_name() == "Pawn" and figure.get_color == "White" and figure.get_en_passant() is True:
                        possible_moves.append((index + 1, letter + 1))
        return possible_moves

    # returns all possible moves a bishop can make from his position
    def possible_bishop_moves(self, own_position, destination, color):
        possible_moves = []
        index = own_position[0]
        letter = own_position[1]
        range = [1,2,3,4,5,6,7,8]

        # following flags represent 4 quadrants of a coordinate system which has own_position as source
        # if quadrant flag is False, Board won't check for possible moves in that quadrant
        first_quadrant = True
        second_quadrant = True
        third_quadrant = True
        fourth_quadrant = True

        for i in range(1,8):
            if first_quadrant:
                if index + i in range and letter + i in range:
                    if self.board[index+i][letter+i].is_occupated():
                        figure = self.board[index+i][letter+i].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index+i, letter+i))
                        first_quadrant = False
                    else:
                        possible_moves.append((index+i, letter+i))
            if second_quadrant:
                if index + i in range and letter - i in range:
                    if self.board[index+i][letter-i].is_occupated():
                        figure = self.board[index+i][letter-i].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index+i, letter-i))
                        second_quadrant = False
                    else:
                        possible_moves.append((index+i, letter-i))
            if third_quadrant:
                if index - i in range and letter + i in range:
                    if self.board[index-i][letter+i].is_occupated():
                        figure = self.board[index-i][letter+i].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index-i, letter+i))
                        third_quadrant = False
                    else:
                        possible_moves.append((index-i, letter+i))
            if fourth_quadrant:
                if index - i in range and letter - i in range:
                    if self.board[index-i][letter-i].is_occupated():
                        figure = self.board[index-i][letter-i].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index-i, letter-i))
                        fourth_quadrant = False
                    else:
                        possible_moves.append((index-i, letter-i))
        return possible_moves

    # returns all possible moves a rook can make from his position
    def possible_rook_moves(self, own_position, color):
        possible_moves = []
        index = own_position[0]
        letter = own_position[1]
        range = [1, 2, 3, 4, 5, 6, 7, 8]

        # following flags represent 4 quadrants of a coordinate system which has own_position as source
        # if quadrant flag is False, Board won't check for possible moves in that quadrant
        first_quadrant = True
        second_quadrant = True
        third_quadrant = True
        fourth_quadrant = True

        for i in range(1, 8):
            if first_quadrant:
                if index in range and letter + i in range:
                    if self.board[index][letter + i].is_occupated():
                        figure = self.board[index][letter + i].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index, letter + i))
                        first_quadrant = False
                    else:
                        possible_moves.append((index, letter + i))
            if second_quadrant:
                if index + i in range and letter in range:
                    if self.board[index + i][letter].is_occupated():
                        figure = self.board[index + i][letter].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index + i, letter))
                        second_quadrant = False
                    else:
                        possible_moves.append((index + i, letter))
            if third_quadrant:
                if index in range and letter - i in range:
                    if self.board[index][letter - i].is_occupated():
                        figure = self.board[index][letter - i].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index, letter - i))
                        third_quadrant = False
                    else:
                        possible_moves.append((index, letter - i))
            if fourth_quadrant:
                if index - i in range and letter in range:
                    if self.board[index - i][letter].is_occupated():
                        figure = self.board[index - i][letter].get_figure()
                        fig_color = figure.get_color()
                        if (color == "Black" and fig_color == "White") or (color == "White" and fig_color == "Black"):
                            possible_moves.append((index - i, letter))
                        fourth_quadrant = False
                    else:
                        possible_moves.append((index - i, letter))
        return possible_moves

    # returns all possible moves a knight can make from his position
    def possible_knight_moves(self, own_position, color):
        possible_moves = []
        index = own_position[0]
        letter = own_position[1]
        range = [1,2,3,4,5,6,7,8]

        if index + 2 in range and letter + 1 in range:
            if self.board[index+2][letter+1].is_occupated():
                figure = self.board[index+2][letter+1].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index+2, letter+1))
            else:
                possible_moves.append((index + 2, letter + 1))
        if index + 2 in range and letter - 1 in range:
            if self.board[index+2][letter-1].is_occupated():
                figure = self.board[index+2][letter-1].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index+2, letter-1))
            else:
                possible_moves.append((index + 2, letter - 1))
        if index - 2 in range and letter + 1 in range:
            if self.board[index-2][letter+1].is_occupated():
                figure = self.board[index-2][letter+1].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index-2, letter+1))
            else:
                possible_moves.append((index - 2, letter + 1))
        if index - 2 in range and letter - 1 in range:
            if self.board[index-2][letter-1].is_occupated():
                figure = self.board[index-2][letter-1].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index-2, letter-1))
            else:
                possible_moves.append((index - 2, letter - 1))
        if index + 1 in range and letter + 2 in range:
            if self.board[index+1][letter+2].is_occupated():
                figure = self.board[index+1][letter+2].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index+1, letter+2))
            else:
                possible_moves.append((index + 1, letter + 2))
        if index + 1 in range and letter - 2 in range:
            if self.board[index+1][letter-2].is_occupated():
                figure = self.board[index+1][letter-2].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index+1, letter-2))
            else:
                possible_moves.append((index + 1, letter - 2))
        if index - 1 in range and letter + 2 in range:
            if self.board[index-1][letter+2].is_occupated():
                figure = self.board[index-1][letter+2].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index-1, letter+2))
            else:
                possible_moves.append((index - 1, letter + 2))
        if index - 1 in range and letter - 2 in range:
            if self.board[index-1][letter-2].is_occupated():
                figure = self.board[index-1][letter-2].get_figure()
                if (color == "White" and figure.get_color() == "Black") or (color == "Black" and figure.get_color() == "White"):
                    possible_moves.append((index-1, letter-2))
            else:
                possible_moves.append((index - 1, letter - 2))
        return possible_moves

    # returns all possible moves a king can make from his position
    def possible_king_moves(self, own_position, color):
        possible_moves = []
        index = own_position[0]
        letter = own_position[1]
        range = [1, 2, 3, 4, 5, 6, 7, 8]

        return possible_moves

    # returns all possible moves a queen can make from her position
    def possible_queen_moves(self, own_position, color):
        possible_moves = []
        index = own_position[0]
        letter = own_position[1]
        range = [1, 2, 3, 4, 5, 6, 7, 8]

        return possible_moves




