#!/usr/bin/env python
"""Provides A GUI for specific Machine Learning Use-cases.

TF_Curses is a frontend for processing datasets into machine
learning models for use in predictive functions.
"""
__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

import curses
import curses.panel
import os
import sys
import datetime
from time import sleep

def get_time():
    return datetime.datetime.now().replace(microsecond=0).isoformat().replace('T', ' ')


class Window(object):
    def __init__(self, stdscr):
        self.screen = stdscr
        stdscr.box()
        title = "TF_Curses | An AplhaGriffin Project | 2017 |"
        sub_title = " py_version | tf_version | {}".format(get_time())
        # dont forget x and y are backwards... ie y, x
        stdscr.addstr(2, 2, title + sub_title)
        self.screen.hline(3, 2, curses.ACS_HLINE, 90)
        self.running = True
        self.main_loop()

    def main_loop(self):
        # create panels
        text_panel = self.text_outpanel(8, 8)
        text_panel.top()
        while self.running:
            curses.panel.update_panels()
            self.screen.refresh()
            sleep(.1)

    def text_outpanel(self, x, y, h=20, w=40, file=None):
        if file is None:
            filename = "sample.txt"
            filepath = "/home/eric/repos/pycharm_repos/tf_utilities/scratch"
            file = os.path.join(filepath, filename)
        text = open(file, "r", encoding='utf-8').read()
        win, panel = self.make_panel(h, w, y, x,
                                     label=filename)

        win.scrollok(True)
        win.addstr(2, 2, text)
        return panel

    def make_panel(self, h, l, y, x, label, scroll=False):
        win = curses.newwin(h, l, y, x)
        win.erase()
        win.box()
        # this should be true is addstring throws an error
        win.scrollok(scroll)
        win.addstr(1, 1, str(label))
        panel = curses.panel.new_panel(win)
        return win, panel

    def main_test(self):
        win1, panel1 = self.make_panel(10, 12, 5, 5, "Panel 1")
        win2, panel2 = self.make_panel(10, 12, 8, 8, "Panel 2")
        curses.panel.update_panels()
        self.screen.refresh()
        sleep(1)
        panel1.top()
        curses.panel.update_panels()
        self.screen.refresh()
        sleep(1)

        for i in range(13):
            panel2.move(8, 8 + i)
            curses.panel.update_panels()
            self.screen.refresh()
            sleep(0.1)

        sleep(5)
        return True


if __name__ == '__main__':
    try:
        os.system('clear')
        curses.wrapper(Window)
        print("Alldone! Alphagriffin.com")

    except KeyboardInterrupt:
        os.system('clear')
        sys.exit("AlphaGriffin.com")
