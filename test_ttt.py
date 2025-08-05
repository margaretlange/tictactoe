import pytest
from tictactoe import Board, Player, BadSquareError, toggle_player
from boards import horizontal_one, horizontal_two, vertical_one, vertical_two, left_to_right, right_to_left
import pdb


def test_create_board():
    my_board = Board()
    assert my_board is not None


def test_create_player():
    my_player = Player('O', 'Maggie')
    assert my_player is not None


# @pytest.mark.skip(reason="just for now")
@pytest.mark.parametrize("input_board", [
        horizontal_one,
        horizontal_two,
        vertical_one,
        vertical_two,
        left_to_right,
        right_to_left
    ])
def test_all(input_board):
    # pdb.set_trace()
    board_setup, board_winner = input_board
    my_board = Board()
    my_board.set_board(board_setup)
    winner, is_win = my_board.is_game_over()
    assert is_win
    assert winner == board_winner


def test_player_exists():
    my_board = Board()
    my_player = Player("X", "Alice")
    my_player.set_board(my_board)
    assert my_player


def test_play_square():
    my_board = Board()
    my_player = Player("X", "Alice")
    my_player.set_board(my_board)
    my_player.play_round(0, 1)
    assert my_board.board[0][1] == 'X'


def test_square_already_occupied():
    my_board = Board()
    my_board.set_board(right_to_left[0])
    my_player = Player("X", "Alice")
    my_player.set_board(my_board)
    with pytest.raises(BadSquareError):
        my_player.play_round(0, 1)


def test_square_out_of_bounds():
    my_board = Board()
    my_player = Player("X", "Alice")
    my_player.set_board(my_board)
    with pytest.raises(BadSquareError):
        my_player.play_round(3, 3)


def test_toggle_player():
    player_X = Player("X", "Alice")
    player_O = Player("O", "Bob")
    toggled_one = toggle_player(player_X, player_O, player_O)
    assert toggled_one.symbol == "X"
    toggled_two = toggle_player(player_X, player_O, player_X)
    assert toggled_two.symbol == "O"
