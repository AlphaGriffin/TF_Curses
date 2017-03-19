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

import http.server
import socketserver
import sys

class Handler(http.server.SimpleHTTPRequestHandler):

    def write(self, message=""):
        self.message = message
        return True

    def do_GET(self):
        try:
            message = self.message
        except:
            message = "Please Try again."
            pass
        # Construct a server response.
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))
        return


def main(argz):
    _input = ""
    _h = Handler
    currentlyrunning = True
    while currentlyrunning:
        try:
            print("Server Running")
            httpd = socketserver.TCPServer(('', 10420), _h)
            httpd.handle_request()

        except KeyboardInterrupt as e:
            _input = e
            print(e)
            pass

    if _input is not "" or _input is not "a":
        print("??")

    if _input is "x":
        sys.exit()

    print("this is working")
