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

    figure = board.update_board((1,7), (3,6))
    board.update_board((8, 2), (6, 3))
    if figure is not None:
        if figure.get_color() == "Black":
            black_player.remove_piece(figure)
        else:
            white_player.remove_piece(figure)
    board.update_board((3,6), (5,5))
    board.print_board()
    print(board.possible_knight_moves((5,5), "White"))



