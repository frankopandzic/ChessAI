class Pawn:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0
        self.en_passant_possible = False
        self.promotion_possible = False

    def set_en_passant(self, bool):
        self.en_passant_possible = bool

    def get_en_passant(self):
        return self.en_passant_possible

    def update_move_counter(self):
        self.move_counter += 1

    def get_move_counter(self):
        return self.move_counter

    def get_name(self):
        return "Pawn"

    def set_promotion_possible(self, bool):
        self.promotion_possible = bool

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"


class Bishop:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position

    def get_name(self):
        return "Bishop"

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"


class Knight:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position

    def get_name(self):
        return "Knight"

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"


class Rook:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0
        self.castling_possible = True

    def set_castling_false(self):
        self.castling_possible = False

    def get_castling(self):
        return self.castling_possible

    def update_move_counter(self):
        self.move_counter += 1

    def get_move_counter(self):
        return self.move_counter

    def get_name(self):
        return "Rook"

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"


class Queen:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position

    def get_name(self):
        return "Queen"

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"


class King:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0
        self.castling_possible = True

    def set_castling_false(self):
        self.castling_possible = False

    def get_castling(self):
        return self.castling_possible

    def update_move_counter(self):
        self.move_counter += 1

    def get_move_counter(self):
        return self.move_counter

    def get_name(self):
        return "King"

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"
