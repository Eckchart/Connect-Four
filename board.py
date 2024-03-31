import unittest
import string
import random


class Board:
    def __init__(self, nr_rows=6, nr_cols=7):
        self._nr_rows = nr_rows
        self._nr_cols = nr_cols
        self._board = [[' ' for _ in range(self.nr_cols)] for _ in range(self.nr_rows)]  # 6 x 7 gameboard.

    @property
    def nr_rows(self):
        return self._nr_rows
    
    @property
    def nr_cols(self):
        return self._nr_cols
    
    def get(self, row: int, col: int) -> str:
        """
        Returns the value of the board at coordinates (row, col).

        @param row - int: the input row of the board;
        @param col - int: the input column of the board.
        @Raises:
        - ValueError if the given coordinates are outside the board.
        """
        if not 0 <= row < self.nr_rows or not 0 <= col < self.nr_cols:
            raise ValueError("Outside board.")
        return self._board[row][col]

    def set_board(self, symbol: str, row: int, col: int) -> None:
        """
        Sets the value of the board at coordinates (row, col) to value 'symbol'.

        @param symbol - str: what the board will be equal to at coordinates (row, col);
        @param row - int: the input row of the board;
        @param col - int: the input column of the board.
        """
        self._board[row][col] = symbol

    def is_won(self) -> bool:
        """
        Checks if the board, in its current state, is won (by either player).

        @return True if either player won, False otherwise.
        """
        # check rows
        for row in self._board:
            j = 0
            while j + 3 < self.nr_cols:
                if row[j] == ' ':
                    j += 1
                    continue
                if row[j] == row[j + 1] == row[j + 2] == row[j + 3]:
                    return True
                j += 1
        # check columns
        for j in range(7):
            i = 0
            while i + 3 < self.nr_rows:
                if self.get(i, j) == ' ':
                    i += 1
                    continue
                if self.get(i, j) == self.get(i + 1, j) == self.get(i + 2, j) == self.get(i + 3, j):
                    return True
                i += 1
        # check diagonals
        # of the form '\'
        i = 0
        while i + 3 < self.nr_rows:
            j = 0
            while j + 3 < self.nr_cols:
                if self.get(i, j) == ' ':
                    j += 1
                    continue
                if self.get(i, j) == self.get(i + 1, j + 1) == self.get(i + 2, j + 2) == self.get(i + 3, j + 3):
                    return True
                j += 1
            i += 1
        # of the form '/'
        i = 3
        while i < self.nr_rows:
            j = 0
            while j + 3 < self.nr_cols:
                if self.get(i, j) == ' ':
                    j += 1
                    continue
                if self.get(i, j) == self.get(i - 1, j + 1) == self.get(i - 2, j + 2) == self.get(i - 3, j + 3):
                    return True
                j += 1
            i += 1
        return False

    def is_tie(self) -> bool:
        """
        Checks if the board, in its current state, is in a tie.

        @return True if the board is in a tie, False otherwise.
        """
        cond = True
        for col in range(0, self.nr_cols):
            cond &= self.get(0, col) != ' '
        return cond

    def update(self, symbol: str, col: int) -> None:
        """
        Makes a move at column 'col', placing the symbol 'H' if the move was
        done by a human, else 'C' if it was done by the computer.

        @param symbol - str: the symbol to place;
        @param col - int: the column to place the symbol in.
        @Raises:
        - ValueError if the given column is outside the board or if the column is full.
        """
        if not 0 <= col < self.nr_cols:
            raise ValueError("Outside board.")
        if self.get(0, col) != ' ':
            raise ValueError("Invalid column.")
        res_row = self.nr_rows - 1
        while True:
            if self.get(res_row, col) == ' ':
                break
            res_row -= 1
        self._board[res_row][col] = symbol

    def __str__(self) -> str:
        """
        Returns the string representation of the current board.

        @return the current board, as a string.
        """
        res = ""
        for nr in range(1, self._nr_cols):
            res += f"{nr} "
        res += f"{self._nr_cols}\n"
        for row in self._board:
            for elem in row:
                res += elem + ' '
            res += '\n'
        return res[:-1]  # '[:-1]' in order to ignore the last newline.


class TestBoard(unittest.TestCase):
    def test_set(self):
        board = Board()
        board.set_board('H', 2, 3)
        self.assertEqual(board.get(2, 3), 'H')

    def test_is_won(self):
        board = Board()
        board.update('H', 1)
        board.update('H', 2)
        board.update('H', 3)
        board.update('H', 4)
        self.assertTrue(board.is_won())

    def test_is_tie(self):
        board = Board()
        for _ in range(board.nr_rows):
            for col in range(board.nr_cols):
                board.update(random.choice(string.ascii_uppercase), col)
        self.assertTrue(board.is_tie())


if __name__ == "__main__":
    unittest.main()
