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

import os
import sys
from datetime import datetime
from time import sleep
from threading import Thread
import ag.logging as log
import ag.tf_curses.server.basic_server as serv
import ag.tf_curses.chatbot.chatbot as chatbot
import ag.tf_curses.server.tf_server as tf_server

def TF_Server():
    try:
        server = tf_server.tfserver()
        Thread(target=server.start_server).start()
    except:
        log.error("and thats okay too.")

def Chatbot():
    service = chatbot.chatbot()
    return service

def Sock_Server(host, port, service=None):
    server = serv.Sock_Server(host, port, service)
    try:
        Thread(target=server.start_server).start()
        log.info("this is working! Server Started")
    except:
        log.error("BUMMER!!")



def main():
    pid = os.getpid()
    host = "127.0.0.1"
    port = 12345
    mesg = "Starting TF_Server\n-\tTime: {}\n\tPID: {}\n\tServer- {}:{}".format(
        datetime.now().isoformat(timespec='minutes'), pid, host, port)
    log.info(mesg)
    chat_service = Chatbot()
    Sock_Server(host, port, chat_service)

    # and for the heck of it... managa a TF server_session too... just in case
    TF_Server()

    # this should have a hold out loop... shouldnt it???

if __name__ == '__main__':
    try:
        main()
    except:
        log.error("and thats okay too.")