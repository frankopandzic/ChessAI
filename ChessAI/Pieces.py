class Pawn:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0

    def get_name(self):
        return "Pawn"


class Bishop:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0

    def get_name(self):
        return "Bishop"


class Knight:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0

    def get_name(self):
        return "Knight"


class Rook:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0

    def get_name(self):
        return "Rook"


class Queen:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0

    def get_name(self):
        return "Queen"


class King:
    def __init__(self, bool, starting_position):
        # boolean - if True then it is a white piece, black piece otherwise
        self.white = bool
        # tuple - first element is the letter of square position,
        # second element is index of square position,
        # e.g. - starting_position = ('b', 2)
        self.position = starting_position
        self.move_counter = 0

    def get_name(self):
        return "King"
