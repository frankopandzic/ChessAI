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

    board.update_board((7, 2), (4, 2))
    board.update_board((2, 3), (4, 3))
    board.print_board()
    print(board.legal_move((1,5), (1,7)))
    print(board.get_possible_moves("Pawn", (4,2), "Black"))

