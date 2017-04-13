#!/usr/bin/env python
""" Chat Client Lite
A chat client for the AGDummy
in the most basic sense.
in an intuitive to use manner.
"""
__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

import os, sys, datetime
import socket
from time import sleep
import ag.logging as log
log.set(5)
"""
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.connect(("localhost", 12345))
clients_input = input("Send Chat Message:\n")
soc.send(clients_input.encode("utf8")) # we must encode the string to bytes
result_bytes = soc.recv(4096) # the number means how the response can be in bytes
result_string = result_bytes.decode("utf8") # the return will be in bytes, so decode

print("Result from server is {}".format(result_string))
"""
class AGDummyClientLite(object):
    def __init__(self):
        self.connected = False
        self.connect()

    def connect(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect(("localhost", 12345))
        self.connected = True

    @property
    def is_connected(self):
        return self.connected

    def send_msg(self, msg):
        self.soc.send(msg.encode('UTF-8'))
        return True

    def recv_msg(self):
        return self.soc.recv(4096).decode('UTF-8')

    def main(self):
        log.info("Starting AGDummy Chat Client")
        tests = ["This is long test",
                 "this good test",
                 "Lincoln saw that",
                 "Bad Test",
                 "close"]
        while self.is_connected:
            for i in range(5):
                self.send_msg("x={}".format(tests[i]))
                response = self.recv_msg()
                print("Testing: {}\nresponse: {}".format(tests[i],
                                                         response))
                sleep(1.5)
            self.connected = False
        return True



if __name__ == '__main__':
    try:
        app = AGDummyClientLite()
        if app.main(): pass
            #foo(bar)
        else:
            log.fatal("bummer")
            sys.exit("Lame Crashing..")

    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        log.info("Respectfully crashing now...")
        log.fatal("{}\n{}\n{}".format(exc_type,
                                      exc_obj,
                                      exc_tb))
