from Board import Board
from ChessPlayer import ChessPlayer


if __name__ == '__main__':
    board = Board()
    white_player = ChessPlayer(True)
    black_player = ChessPlayer(False)

    white_pieces = board.get_white_pieces()
    black_pieces = board.get_black_pieces()

    white_player.set_pieces(white_pieces)
    black_player.set_pieces(black_pieces)

    chessboard = board.get_board()
    num_of_possible_moves = 0
    for i, row in enumerate(chessboard):
        for j, square in enumerate(row):
            if square.is_occupated():
                figure = square.get_figure()
                name = figure.get_name()
                color = figure.get_color()
                if name == "Pawn":
                    num_of_possible_moves += len(board.possible_pawn_moves((i+1, j+1), color))
                elif name == "Rook":
                    num_of_possible_moves += len(board.possible_rook_moves((i + 1, j + 1), color))
                elif name == "Bishop":
                    num_of_possible_moves += len(board.possible_bishop_moves((i + 1, j + 1), color))
                elif name == "Knight":
                    num_of_possible_moves += len(board.possible_knight_moves((i + 1, j + 1), color))
                elif name == "Queen":
                    num_of_possible_moves += len(board.possible_queen_moves((i + 1, j + 1), color))
                elif name == "King":
                    num_of_possible_moves += len(board.possible_king_moves((i + 1, j + 1), color))
    print(num_of_possible_moves)




