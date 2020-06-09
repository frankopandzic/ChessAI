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

    white_pieces = white_player.get_pieces()
    for key in white_pieces:
        for piece in white_pieces[key]:
            print(piece.get_name())
    print()
    figure = board.board[1][1].get_figure()
    white_player.remove_piece(figure)
    white_pieces = white_player.get_pieces()
    for key in white_pieces:
        for piece in white_pieces[key]:
            print(piece.get_name())

