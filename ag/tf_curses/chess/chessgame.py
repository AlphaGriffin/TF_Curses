"""TF_Curses Project.

AG_Chess game in the TF_Curses project.
"""

import sys
import numpy as np

class AgChess(object):
    """AG Chess Game object."""

    def __init__(self):
        """Initialize a board with 2 players."""
        self.board = 0
        self.player0 = 0
        self.player1 = 0
        self.start_positions()
        # self.build_board()

    def main(self):
        """A test object."""
        self.player = 1
        return True

    def start_positions(self):
        """Start a new game."""
        player0 = np.chararray((8, 8))
        start_p = ['R', 'J', 'B', 'Q', 'K', 'B', 'J', 'R']
        for index, row in enumerate(player0):
            if index is 0:
                for r_index, square in enumerate(row):
                    row[r_index] = start_p[r_index]
            elif index is 1:
                for r_index, square in enumerate(row):
                    row[r_index] = "P"
            else:
                for r_index, square in enumerate(row):
                    row[r_index] = ''
        self.player0 = player0
        # start 2nd player
        player1 = np.chararray((8, 8))
        for index, row in enumerate(player1):
            if index is player1.shape[0]-1:
                for r_index, square in enumerate(row):
                    row[r_index] = start_p[r_index]
            elif index is player1.shape[0]-2:
                for r_index, square in enumerate(row):
                    row[r_index] = "P"
            else:
                for r_index, square in enumerate(row):
                    row[r_index] = ''
        self.player1 = player1
        self.board = self.player0 + self.player1
        for index, row in enumerate(self.board):
            for r_index, square in enumerate(row):
                if square is '':
                    self.board[index, r_index] = 0

    def build_board(self):
        """Construct proper placement of colored squares."""
        self.board = self.player0 + self.player1
        for index, row in enumerate(self.board):
            for r_index, square in enumerate(row):
                if square is '':
                    self.board[index, r_index] = 0


def main():
    """Build and run a test."""
    app = AgChess()
    if app.main():
        print(app.board.decode('UTF-8'))
        sys.exit('All systems passed.')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.exit("Alphagriffin.com\n{}".format(e))
