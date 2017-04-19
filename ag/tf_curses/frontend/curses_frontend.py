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

import os, sys, time
import curses
import curses.panel
import ag.logging as log


class Window(object):
    def __init__(self, stdscr=None):
        # this is passed with the Curses Wrapper for testing
        if stdscr is None:
            stdscr = curses.initscr()
        self.screen = stdscr
        curses.start_color()
        self.setup_color()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1)
        self.screen_h, self.screen_w = self.screen.getmaxyx()
        self.screen_mode = True

    def get_input(self):
        x = 0
        self.footer[0].addstr(1, 1, "Mode: KeyStroke")
        self.screen.nodelay(True)
        if self.screen_mode:
            x = self.screen.getch()
        else:
            self.screen.keypad(0)
            curses.echo()
            self.redraw_window(self.footer)
            x = self.footer[0].getstr(1,1).decode('UTF-8')
            self.screen.keypad(1)
            curses.noecho()
            self.screen_mode = True
            self.redraw_window(self.footer)
        return x

    def setup_color(self):
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        self.color_rw = curses.color_pair(1)
        curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
        self.color_cb = curses.color_pair(2)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        self.color_gb = curses.color_pair(3)
        self.color_bold = curses.A_BOLD
        self.color_blink = curses.A_BLINK
        self.color_error = self.color_bold | self.color_blink | self.color_rw
        return True

    def refresh(self):
        # TODO: add screensize checker!
        #
        # curses.resizeterm(y, x)
        self.screen.refresh()
        curses.panel.update_panels()
        return True

    def end_safely(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()
        return True

    def main_screen(self):
        h = self.screen_h
        w = self.screen_w

        header_dims = [3, w, 0, 0]
        split = int(w / 3) - 1
        winleft_dims = [h-3-4-3, split, 3, 0]
        self.winright_dims = [h-3-4-3, w - split-1, 3, split + 1]
        footer_dims = [3, w, h-3, 0]
        debug_dims = [4, w, h-7, 0]
        self.header = self.make_panel(header_dims, "header")
        self.winleft = self.make_panel(winleft_dims, "options", True)
        self.winright = self.make_panel(self.winright_dims, "screen", True)
        self.debug = self.make_panel(debug_dims, "debugs", True)
        self.footer = self.make_panel(footer_dims, "interface", True)
        curses.panel.update_panels()
        self.screen.addstr(h-1,w-9,"<{},{}>".format(h, w))
        self.screen.refresh()

    def make_panel(self, dims, label, scroll=False):
        options = 0
        win = curses.newwin(dims[0], dims[1], dims[2], dims[3])
        win.scrollok(scroll)
        panel = curses.panel.new_panel(win)
        self.redraw_window([win, panel, label])
        return win, panel, label, options

    def redraw_window(self, win):
        win[0].erase()
        win[0].box()
        win[0].addstr(0, 1, str("| {} |".format(win[2])))

    def main_test(self):
        win1, panel1 = self.make_panel([10, 12, 5, 5], "Panel 1")
        win2, panel2 = self.make_panel([10, 12, 8, 8], "Panel 2")
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
