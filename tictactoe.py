# import pdb


class BadSquareError(Exception):
    """Exception raised when an invalid square is played."""


class Board:
    """
    Represents a Tic-Tac-Toe board.

    Attributes:
        board (list): A 3x3 grid representing the game board.
        winner (str): The symbol of the winning player, if any.
        game_over (bool): Indicates if the game is over.
        turns (int): The number of turns played.
    """

    def __init__(self):
        """Initializes the board and game state."""
        self.board = []
        self.winner = None
        self.game_over = False
        self.turns = 0
        self.init_board()

    def __str__(self):
        """
        Returns a string representation of the board.

        Empty squares are represented by 'E'.
        """
        total = []
        for row in self.board:
            as_strs = ["E" if not s else s for s in row]
            total.append(" ".join(as_strs))
        return "\n".join(total)

    def set_board(self, board_string):
        """
        Sets the board state from a string representation.
        Used for testing.

        Args:
            board_string (str): A string representation of the board.
        """
        string_rows = board_string.split("\n")
        new_board = []
        for str_row in string_rows:
            row = str_row.split()
            new_board.append(row)
        self.board = new_board

    def init_board(self):
        """Initializes the board to a 3x3 grid of None values."""
        for i in range(3):
            row = []
            for j in range(3):
                row.append(None)
            self.board.append(row)
        self.game_over = False
        self.turns = 0

    def set_round(self, row, col, symbol):
        """
        Sets a player's move on the board.

        Args:
            row (int): The row index of the square.
            col (int): The column index of the square.
            symbol (str): The player's symbol ('X' or 'O').

        Raises:
            BadSquareError: If the square is out of bounds or already taken.
        """
        if row < 0 or row > 2 or col < 0 or col > 2:
            raise BadSquareError(f"{row}, {col} is out of bounds!")
        if self.board[row][col]:
            raise BadSquareError(f"Square {row}, {col} is already taken!")
        self.board[row][col] = symbol
        self.turns += 1

    def horizontal_win(self):
        """
        Checks for a horizontal win.

        Returns:
            bool: True if a horizontal win is found, False otherwise.
        """
        for row in self.board:
            start = row[0]
            if start and row[1] == start and row[2] == start:
                self.winner = start
                self.game_over = True
                return True
        return False

    def vertical_win(self):
        """
        Checks for a vertical win.

        Returns:
            bool: True if a vertical win is found, False otherwise.
        """
        for col in zip(*self.board):
            start = col[0]
            if start and col[1] == start and col[2] == start:
                self.winner = start
                self.game_over = True
                return True
        return False

    def left_to_right_win(self):
        """
        Checks for a diagonal win from top-left to bottom-right.

        Returns:
            bool: True if a diagonal win is found, False otherwise.
        """
        start = self.board[0][0]
        if start and self.board[1][1] == start and self.board[2][2] == start:
            self.winner = start
            self.game_over = True
            return True
        return False

    def right_to_left_win(self):
        """
        Checks for a diagonal win from top-right to bottom-left.

        Returns:
            bool: True if a diagonal win is found, False otherwise.
        """
        start = self.board[0][2]
        if start and self.board[1][1] == start and self.board[2][0] == start:
            self.winner = start
            self.game_over = True
            return True
        return False

    def diagonal_win(self):
        """
        Checks for any diagonal win.

        Returns:
            bool: True if a diagonal win is found, False otherwise.
        """
        return self.left_to_right_win() or self.right_to_left_win()

    def is_game_over(self):
        """
        Checks if the game is over by checking for horizontal, vertical, or diagonal wins.

        Returns:
            tuple: A tuple containing the winner's symbol (or None) and a boolean indicating if the game is over.
        """
        if self.horizontal_win() or self.vertical_win() or self.diagonal_win():
            return self.winner, True
        elif self.turns == 9:
            return None, True
        else:
            return None, False


class Player:
    """
    Represents a player in the Tic-Tac-Toe game.

    Attributes:
        symbol (str): The player's symbol ('X' or 'O').
        player_name (str): The player's name.
    """

    def __init__(self, symbol, player_name):
        """
        Initializes a player with a symbol and name.

        Args:
            symbol (str): The player's symbol ('X' or 'O').
            player_name (str): The player's name.
        """
        self.symbol = symbol
        self.player_name = player_name

    def __str__(self):
        """Returns the player's name."""
        return self.player_name

    def set_board(self, board):
        """
        Sets the board object for the player.

        Args:
            board (Board): The game board.
        """
        self.board = board

    def play_round(self, row, col):
        """
        Makes a move on the board.

        Args:
            row (int): The row index of the square.
            col (int): The column index of the square.
        """
        self.board.set_round(row, col, self.symbol)


def toggle_player(player_X, player_O, current_player):
    """
    Toggles the current player.

    Args:
        player_X (Player): The player with symbol 'X'.
        player_O (Player): The player with symbol 'O'.
        current_player (Player): The current player.

    Returns:
        Player: The next player.
    """
    if current_player.symbol == player_X.symbol:
        return player_O
    return player_X


if __name__ == "__main__":
    """
    Main function to run the Tic-Tac-Toe game.
    """
    my_b = Board()
    print("Enter name for player O.")
    player_O_name = input()
    print("Enter name for player X.")
    player_X_name = input()

    # Set up players
    player_O = Player("O", player_O_name)
    player_O.set_board(my_b)
    player_X = Player("X", player_X_name)
    player_X.set_board(my_b)
    players_dict = {"X": player_X, "O": player_O}
    player_with_turn = player_X

    # Play a game
    while True:
        print(my_b)
        print(
            f"Player {player_with_turn.player_name}, enter the row number of the square you want to play."
        )
        row = input()
        print(
            f"Player {player_with_turn.player_name}, enter the column number of the square you want to play."
        )
        col = input()
        try:
            player_with_turn.play_round(int(row), int(col))
        except BadSquareError:
            print(f"Sorry! Square ({row}, {col}) is not an option. Please try again.")
            continue
        winner_symbol, res = my_b.is_game_over()
        if res:
            if winner_symbol:
                print(f"Congratulations, {players_dict[winner_symbol]}! You won!")
            else:
                print("The game is a draw!")
            print("Final board:")
            print(my_b)
            break
        player_with_turn = toggle_player(player_X, player_O, player_with_turn)
