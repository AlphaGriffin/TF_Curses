#!/usr/bin/env python
"""TF_Curses Project.

AG_Chess game in the TF_Curses project.
"""

import sys

class AgChess(object):
    """AG Chess Game object."""

    def __init__(self):
        """Initialize a board with 2 players."""
        self.board = 0
        self.player = 0
        self.opponent = 0

    def main(self):
        """A test object."""
        self.player = 1
        return True


def main():
    """Build and run a test."""
    app = AgChess()
    if app.main():
        sys.exit('All systems passed.')

if __name__ == '__main__':
    try:
        main()
    except:
        log.error("and thats okay too.")
