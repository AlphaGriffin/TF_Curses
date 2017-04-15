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

import os, sys, datetime, time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
import ag.logging as log
import database_interface as DB
log.set(5)

class App(object):
    def __init__(self):
        log.info("AGTF seq Starting To Build Model")
        self.database = DB.Database(db=2)


    def main(self, args):
        self.database.write_data("test", 420)
        x = self.database.read_data("test")
        log.debug(x)
        return True





if (__name__ == '__main__'):
    try:
        os.system('clear')
        app = App()
        if app.main(sys.argv):
            log.info("Everything Checks out.")

        else:
            sys.exit("Thanks A lot for trying Alphagriffin.com")
        log.warn("Alldone! Alphagriffin.com")

    except KeyboardInterrupt:
        os.system('clear')
        sys.exit("AlphaGriffin.com")