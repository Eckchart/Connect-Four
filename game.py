from board import Board
import random


class ComputerPlayer:
    def play_computer(self, board: Board) -> None:
        """
        Makes a move for the computer player.

        @param board - Board: the current gameboard.
        """
        avail_cols = []
        for col in range(board.nr_cols):
            if board.get(0, col) == ' ':
                avail_cols.append(col)
        # See if computer is 1 move away from winning.
        for col in avail_cols:
            board.update('C', col)
            if board.is_won():
                return
            for row in range(board.nr_rows):
                if board.get(row, col) == 'C':
                    board.set_board(' ', row, col)
                    break

        # Else see if computer can block human player's 1-move victory.
        for col in avail_cols:
            board.update('H', col)
            for row in range(board.nr_rows):
                if board.get(row, col) == 'H':
                    if board.is_won():
                        board.set_board('C', row, col)
                        return
                    else:
                        board.set_board(' ', row, col)
                        break

        # Else make a random move.
        board.update('C', random.choice(avail_cols))


class Game:
    def __init__(self, board: Board, computer_player: ComputerPlayer):
        self._board = board
        self._computer_player = computer_player

    def get_board(self) -> str:
        return str(self._board)

    def is_won(self) -> bool:
        return self._board.is_won()

    def is_tie(self) -> bool:
        return self._board.is_tie()
    
    def play_human(self, col: int) -> None:
        """
        Updates the gameboard with the move made by the human.

        @param col - int: the column in which the human made a move.
        """
        self._board.update('H', col)
    
    def play_computer(self) -> None:
        """
        Makes a move with the computer player.
        """
        self._computer_player.play_computer(self._board)


if __name__ == "__main__":
    print(Game(Board(), ComputerPlayer()).get_board())
