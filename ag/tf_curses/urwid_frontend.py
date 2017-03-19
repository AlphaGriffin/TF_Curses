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

import sys
import urwid

class App(object):
    def __init__(self):
        self.txt = urwid.Text("AlphaGriffin.com")

        self.fill = urwid.Filler(self.txt, 'top')
        self.loop = urwid.MainLoop(self.fill, unhandled_input=self.show_or_exit)
        self.bannerLoop = self.showbanner()
        self.bannerLoop2 = self.showbanner2()
        # boolean button toggles
        self.button_b = False
        self.button_p = False

    def showbanner(self):
        palette = [
            ('banner', 'black', 'light gray'),
            ('streak', 'black', 'dark red'),
            ('bg', 'black', 'dark blue'), ]
        self.banner = urwid.Text(('banner', u" Hello World "), align='center')
        map1 = urwid.AttrMap(self.banner, 'streak')
        fill = urwid.Filler(map1)
        map2 = urwid.AttrMap(fill, 'bg')
        self.bannerLoop = urwid.MainLoop(map2, palette, unhandled_input=self.show_or_exit)
        self.bannerLoop.run()

    def hidebanner(self):
        self.bannerLoop.stop()

    def showbanner2(self):
        palette = [
            ('banner', '', '', '', '#ffa', '#60d'),
            ('streak', '', '', '', 'g50', '#60a'),
            ('inside', '', '', '', 'g38', '#808'),
            ('outside', '', '', '', 'g27', '#a06'),
            ('bg', '', '', '', 'g7', '#d06'), ]

        placeholder = urwid.SolidFill()
        self.bannerLoop2 = urwid.MainLoop(placeholder, palette, unhandled_input=self.show_or_exit)
        self.bannerLoop2.screen.set_terminal_properties(colors=256)
        self.bannerLoop2.widget = urwid.AttrMap(placeholder, 'bg')
        self.bannerLoop2.widget.original_widget = urwid.Filler(urwid.Pile([]))

        banner2 = urwid.Text(('banner', u" Hello World "), align='center')
        map1 = urwid.AttrMap(banner2, 'streak')
        fill = urwid.Filler(map1)
        map2 = urwid.AttrMap(fill, 'bg')

        self.bannerLoop2.run()

    def hidebanner2(self):
        self.bannerLoop2.stop()

    def startapp(self):
        self.loop.run()

    def show_or_exit(self, key):
        # show banner 1
        if key in ('b', 'B'):
            if self.button_b: self.showbanner()
            else: self.hidebanner()
        # show banner 2
        #  if key in ('p', 'P'):
        #    if self.button_p: self.showbanner2()
        #    else: self.hidebanner2()
        # quit
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()
        # self.txt.set_text(repr(key))
        help =\
        """
        Press Q to quit.
        Press B to toggle banner screen 1.
        Press P to toggle banner screen 2.
        """
        self.txt.set_text("")
