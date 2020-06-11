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

    figure = board.update_board((2,2), (7,2))
    if figure is not None:
        if figure.get_color() == "Black":
            black_player.remove_piece(figure)
        else:
            white_player.remove_piece(figure)
