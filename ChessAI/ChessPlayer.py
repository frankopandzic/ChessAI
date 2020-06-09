class ChessPlayer:
    def __init__(self, bool):
        # boolean which indicates if player has white or black pieces;
        # if True then he has white pieces, black otherwise
        self.white = bool
        self.pieces = {}

    # this method is only called once
    def set_pieces(self, pieces):
        for piece in pieces:
            name = piece.get_name()
            if name in self.pieces:
                self.pieces[name].append(piece)
            else:
                self.pieces[name] = [piece]

    def get_pieces(self):
        return self.pieces

    def remove_piece(self, piece):
        name = piece.get_name()
        self.pieces[name].remove(piece)
