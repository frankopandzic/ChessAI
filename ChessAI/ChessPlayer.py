from decimal import Decimal, ROUND_HALF_UP

class ChessPlayer:
    def __init__(self, bool):
        # boolean which indicates if player has white or black pieces;
        # if True then he has white pieces, black otherwise
        self.white = bool
        self.pieces = {}

        self.pawn_coeff = 1
        self.knight_coeff = 3.3
        self.bishop_coeff = 3.4
        self.rook_coeff = 5.3
        self.queen_coeff = 9.7
        self.move_coeff = 0.1

        self.num_of_moves_ahead = 4

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

    def get_color(self):
        if self.white == False:
            return "Black"
        else:
            return "White"

    def get_opposite_color(self):
        if self.white == False:
            return "White"
        else:
            return "Black"

    def get_pieces_value(self):
        value = 0
        for name in self.pieces:
            if name == "Pawn":
                value += self.pawn_coeff*len(self.pieces[name])
            elif name == "Knight":
                value += self.knight_coeff*len(self.pieces[name])
            elif name == "Bishop":
                length = len(self.pieces[name])
                # paired bishops are worth slightly more than their combined empirical value
                if length > 1:
                    value += 0.5 * self.pawn_coeff
                value += self.bishop_coeff * length
            elif name == "Rook":
                value += self.rook_coeff * len(self.pieces[name])
            elif name == "Queen":
                value += self.queen_coeff * len(self.pieces[name])
        return value

    # evaluate how strong opposition's attacked piece is
    def evaluate_attack(self, square):
        figure = square.get_figure()
        name = figure.get_name()
        if name == "Pawn":
            return self.pawn_coeff/5
        elif name == "Knight":
            return self.knight_coeff/5
        elif name == "Bishop":
            return self.bishop_coeff/5
        elif name == "Rook":
            return self.rook_coeff/5
        elif name == "Queen":
            return self.queen_coeff/5
        else:
            # opposition king is in check
            return self.pawn_coeff

    # returns float value representing current state of the game,
    # e.g. if return_val > 0, player is in a more favorable situation compared to his opposition
    # analogously, if return_val < 0, player is in less favorable situation compared to his opposition
    def evaluate(self, board):
        evaluation = self.get_pieces_value()
        color = self.get_color()

        if color == "White":
            opposition_position = board.get_opposition_position("Black")
        else:
            opposition_position = board.get_opposition_position("White")
        chessboard = board.get_board()

        for index, row in enumerate(chessboard):
            for letter, square in enumerate(row):
                if square.is_occupated():
                    figure = square.get_figure()
                    if figure.get_color() == color:
                        possible_moves = board.get_possible_moves(figure.get_name(), (index + 1, letter + 1), color)
                        if possible_moves:
                            for move in possible_moves:
                                if board.does_it_check((index + 1, letter + 1), move, color):
                                    # if move results in own king being checked, discard that move
                                    evaluation -= self.move_coeff
                            num_of_moves = len(possible_moves)
                            # more possible moves is better
                            # more open position is favorable in this approach
                            evaluation += self.move_coeff * num_of_moves

                        # the more opposition pieces are attacked, the better
                        attacking_moves = [pos for pos in possible_moves if pos in opposition_position]
                        for move in attacking_moves:
                            evaluation += self.evaluate_attack(chessboard[move[0]][move[1]])

        return Decimal(Decimal(evaluation).quantize(Decimal('.0001'), rounding=ROUND_HALF_UP))

    # recursion which searches future moves
    # TO DO: determine start position of possible move, currently we have only end position
    def depth_search(self, player_color, depth, board):
        pass



    # determines optimal move using alpha-beta pruning method
    def make_move(self, board):
        possible_moves = board.get_possible_player_moves(self.get_color())

        for move in possible_moves:
            pass



