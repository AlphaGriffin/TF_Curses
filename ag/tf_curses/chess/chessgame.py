#!/usr/bin/python3
"""TF_Curses Project.

AG_Chess game in the TF_Curses project.
"""

import os
import sys
import numpy as np
import redis
import yaml

__author__      = "Eric Petersen @Ruckusist"
__copyright__   = "Copyright 2017, The Alpha Griffin Project"
__credits__     = ["Eric Petersen",
                   "Shawn Wilson",
                   "@alphagriffin"]
__license__     = "***"
__version__     = "0.0.1"
__maintainer__  = "Eric Petersen"
__email__       = "ruckusist@alphagriffin.com"
__status__      = "Prototype"


class Database_(object):
    """A Copy and paste hack of database interface."""

    def __init__(self, options,
                 host='192.168.99.225',
                 pass_='dummypass', db=0):
        """Testing functionality."""
        self.options = options
        self.database = redis.Redis(
            host=host,
            password=pass_,
            db=db
        )

    def write_data(self, key, value):
        """Testing functionality."""
        self.database.set(key, value)
        return True

    def read_data(self, key):
        """Testing functionality."""
        try:
            value = self.database.get(key).decode('UTF-8')
        except:
            try:
                value = self.database.get(key)
            except Exception as e:
                print("Damnit on the reverse lookup!")
                value = 'unk'
        return value


class Options(object):
    """OH OH DO a yaml file!."""

    def __init__(self, data_path):
        """OH OH DO a yaml file!."""
        config = self.load_options(data_path)
        for i in config:
            setattr(self, '{}'.format(i), '{}'.format(config[i]))

    def load_options(self, data_path):
        """COOL! a yaml file."""
        try:
            with open(data_path, 'r') as config:
                new_config = yaml.load(config)
            return new_config
        except Exception as e:
            print("burn {}".format(e))


class MoveRules(object):
    """This feels wrong.

    It should just know what is a legal move.
    - gotta go with this, U, D, L, R are the moves. And
      E for end point. And then if your piece is there,
      invalid move, if oppenent peice there is a score, if
      nothing is there, its a valie move.
    """

    def __init__(self): pass

    def pawn_rule(): pass

    def rook_rule(): pass

    def knight_rule(): pass

    def bishop_rule(): pass

    def queen_rule(): pass

    def king_rule(): pass


class AgChess(object):
    """AG Chess Game object."""

    def __init__(self):
        """Initialize a board with 2 players."""

        class Player():
            """A player Factory."""

            def __init__(self):
                """Initialize both players.
                And starting positions.
                """
                # a numpy chararray
                self.player_state = np.chararray((8, 8))
                # dict of players remaining pieces.
                self.player_has = {'K': 1,
                                   'Q': 1,
                                   'P': 8}
                # dict of lost pieces.
                self.player_lost = {'K': 0,
                                    'Q': 0,
                                    'P': 0}
                # dict of captured pieces.
                self.player_cap = {'K': 0,
                                   'Q': 0,
                                   'P': 0}

            def start_position55(self):
                start_p = ['R', 'N', 'B', 'Q', 'K', 'B', 'J', 'R']
                for index, row in enumerate(self.player_state):
                    if index is 0:
                        for r_index, square in enumerate(row):
                            row[r_index] = start_p[r_index]
                    elif index is 1:
                        for r_index, square in enumerate(row):
                            row[r_index] = "p"
                    else:
                        for r_index, square in enumerate(row):
                            row[r_index] = ''


        # Initialize some variables
        self.board = 0
        self.player0 = 0
        self.player1 = 0

        # player turn boolean True = Player0
        # make this updateable with a @property
        self.__turn = True

        # startup process
        self.start_positions()

    # $$$$$$$$$$$$$$$$$$$$$$
    # Set Recall Properties
    # $$$$$$$$$$$$$$$$$$$$$$
    @property
    def turn(self):
        """Dont make a comparision to literal.

        For god's sake.
        """
        return self.__turn

    # $$$$$$$$$$$$$$$$$$$$$$
    # Test Functions
    # $$$$$$$$$$$$$$$$$$$$$$
    def main(self):
        """A test object."""
        print(self.board.decode('UTF-8'))
        return True

    # $$$$$$$$$$$$$$$$$$$$$$
    # Game Functions
    # $$$$$$$$$$$$$$$$$$$$$$
    def start_positions(self):
        """Start a new game."""
        player0 = np.chararray((8, 8))
        start_p = ['r', 'n', 'b', 'q', 'k', 'b', 'j', 'r']
        for index, row in enumerate(player0):
            if index is 0:
                for r_index, square in enumerate(row):
                    row[r_index] = start_p[r_index]
            elif index is 1:
                for r_index, square in enumerate(row):
                    row[r_index] = "p"
            else:
                for r_index, square in enumerate(row):
                    row[r_index] = ''
        self.player0 = player0
        # start 2nd player
        player1 = np.chararray((8, 8))
        start_p = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
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

    def make_move(self, mv_to, mv_from, player_turn):
        """Change the board to reflect recent move."""
        # first get whos turn it is.
        if self.turn:
            player = self.player0
            opponent = self.player1
        else:
            player = self.player1
            opponent = self.player0
        # if mv_to has oppenent peice in it... replace it
        # and update score for both players.
        # elif has own peice(it should'nt) fail move.
        # elif





def main():
    """Build and run a test."""
    os.system('clear')
    print("AG_Chess | TF_Curses Project 2017")
    app = AgChess()
    if app.main():
        sys.exit("AG_Chess | TF_Curses Project 2017")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        sys.exit("Alphagriffin.com\n{}".format(e))
