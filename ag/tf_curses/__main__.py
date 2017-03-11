#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffins
# @%@~LICENSE~@%@

"""
TF_Curses
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""
import sys
import urwid


def main(args):
    """The main routine."""
    # tutorial beginnings
    txt = urwid.Text("Hello World")
    fill = urwid.Filler(txt, 'top')
    loop = urwid.MainLoop(fill)
    loop.run()

if __name__ == "__main__":
    main(sys.argv)
