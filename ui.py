import game
import board


class UI():
    def __init__(self, game: game.Game):
        self._game = game
    
    def _print_board(self):
        print(self._game.get_board(), '\n')
    
    def start(self):
        human_move = True
        while True:
            if human_move:
                print("Current state of the game:")
                self._print_board()
                while True:
                    input_col = input("Enter column to make a move in: ")
                    if input_col not in (str(nr + 1) for nr in range(board.Board().nr_cols)):
                        print("Invalid input.\n")
                        continue
                    try:
                        self._game.play_human(int(input_col) - 1)
                    except ValueError as msg:
                        print(msg, '\n')
                    else:
                        print()
                        break
                if self._game.is_won():
                    print("Game was won by HUMAN player, final board:")
                    self._print_board()
                    return
                if self._game.is_tie():
                    print("The game is a TIE, final board:")
                    self._print_board()
                    return
            else:
                self._game.play_computer()
                if self._game.is_won():
                    print("Game was won by COMPUTER player, final board:")
                    self._print_board()
                    return
                if self._game.is_tie():
                    print("The game is a TIE, final board:")
                    self._print_board()
                    return
            human_move ^= 1


if __name__ == "__main__":
    ui = UI(game.Game(board.Board(), game.ComputerPlayer()))
    ui.start()
