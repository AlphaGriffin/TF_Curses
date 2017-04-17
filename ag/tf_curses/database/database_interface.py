#!/usr/bin/env python
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
TF_Curses
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
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

import ag.logging as log

import redis

log.set(5)


class Database(object):
    def __init__(self, host='agserver', pass_='dummypass', db=0):
        self.database = redis.Redis(
            host=host,
            password=pass_,
            db=db
        )

    def main(self):
        if self.database:
            log.debug("found that database")
            if self.write_data('4', '20'):
                log.debug("wrote that data")
                pass
            twenty = self.get_word_by_position(4)
            four = self.get_word_by_position(twenty)
            log.debug("read data test: {}, {}".format(twenty, four))
            if int(float(twenty)) is 4:
                return True

            log.warn("see here... see.")
            return False
        else:
            log.warn("Not logging into the database.")
        return False

    def write_data(self, key, value):
        self.database.set(key, value)
        return True

    def read_data(self, key):
        try:
            value = self.database.get(key).decode('UTF-8')
        except:
            try:
                value = self.database.get(key)
            except Exception as e:
                log.fatal("Damnit on the reverse lookup!")
                value = 'unk'
        return value


if __name__ == '__main__':
    log.info("Starting the Database Testing")
    try:
        app = Database()
        if app.main():
            sys.exit("Everything checks out.")
    except Exception as e:
        log.error("and thats okay too.")
        sys.exit(e)

