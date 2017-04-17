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

import os, sys, time, datetime
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
import curses
import curses.panel
import tensorflow as tf
import ag.logging as log


def get_time():
    return datetime.datetime.now().replace(microsecond=0).isoformat().replace('T', ' ')


class Window(object):
    def __init__(self, stdscr=None):
        if stdscr is None:
            stdscr = curses.initscr()
        self.screen = stdscr
        curses.start_color()
        self.setup_color()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1)
        self.screen.box()
        #title = "AGTFCP | 2017 | {}".format(get_time())
        #sub_title = " Python: {} | Tensorflow: {} | TF_Curses: {}"
        #stdscr.addstr(1, 2, title, self.color_cb)
        #stdscr.addstr(2, 2, sub_title.format(sys.version[0], tf.__version__, __version__), self.color_cb)
        #self.screen.hline(4, 10, curses.ACS_HLINE, 45)
        #/eninit

    def get_input(self):
        x = self.screen.getch()
        log.debug("getting keypress {}".format(x))
        return x

    def setup_color(self):
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
        self.color_rw = curses.color_pair(1)
        curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
        self.color_cb = curses.color_pair(2)
        return True

    def refresh(self):
        curses.panel.update_panels()
        self.screen.refresh()
        return True

    def end_safely(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()
        return True

    def main_loop(self):
        # create panels
        text_panel = self.text_outpanel(8, 8)
        text_panel.top()
        while self.running:
            curses.panel.update_panels()
            self.screen.refresh()
            time.sleep(.1)

    def text_outpanel(self, x, y, h=20, w=40, file=None):
        if file is None:
            filename = "sample.txt"
            filepath = "/home/eric/repos/pycharm_repos/tf_utilities/scratch"
            file = os.path.join(filepath, filename)
        text = open(file, "r", encoding='utf-8').read()
        win, panel = self.make_panel(h, w, y, x,
                                     label=filename)

        win.scrollok(True)
        win.box()
        win.addstr(2, 2, text)
        return panel

    def make_panel(self, h, l, y, x, label, scroll=False):
        win = curses.newwin(h, l, y, x)
        win.erase()
        win.box()
        win.border(2)
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
        time.sleep(1)
        panel1.top()
        curses.panel.update_panels()
        self.screen.refresh()
        time.sleep(1)

        for i in range(13):
            panel2.move(8, 8 + i)
            curses.panel.update_panels()
            self.screen.refresh()
            time.sleep(0.1)

        time.sleep(5)
        return True


if __name__ == '__main__':
    os.system('clear')
    app = Window()
    try:
        app.main_test()
        app.end_safely()
        os.system('clear')
        print("Alldone! Alphagriffin.com")

    except KeyboardInterrupt:
        app.end_safely()
        os.system('clear')
        sys.exit("AlphaGriffin.com")
