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
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
import sys
from datetime import datetime
from time import sleep
from threading import Thread
import ag.logging as log
import ag.tf_curses.server.basic_server as serv
import ag.tf_curses.chatbot.chatbot as chatbot
import ag.tf_curses.server.tf_server as tf_server
import ag.tf_curses.database.database_interface as db
import ag.tf_curses.server.flask_server as flasker

def TF_Server(host, tf_port):
    try:
        server = tf_server.tfserver()
        Thread(target=server.start_server).start()
    except:
        log.error("and thats okay too.")

def Chatbot(database):
    service = chatbot.tf_chatbot(database)
    return service

def Sock_Server(host, port, service=None):
    server = serv.Sock_Server(host, port, service)
    try:
        Thread(target=server.start_server).start()
        log.info("this is working! Server Started")
    except:
        log.error("BUMMER!!")

def Connect_to_remote_database(h, p):
    log.info("Connecting to redis")
    dictionary = db.Database(h, p, db=0)
    rev_dictionary = db.Database(h, p, db=1)
    database = [dictionary, rev_dictionary]
    return database


def main():
    pid = os.getpid()
    # host = "127.0.0.1"
    host = "localhost"
    remote_host = 'agserver'
    remote_pass = 'dummypass'
    chat_port = 12345
    tf_port = 2222
    redis_port = 6379
    mesg = "Starting TF_Curses\n"
    mesg += "Start Time: {}\n".format(datetime.now().isoformat(timespec='minutes'))
    mesg += "PID: {}\n".format(pid)
    log.info(mesg)

    log.info("Starting Redis Server:\t{}:{}".format(remote_host, redis_port))
    db_ = Connect_to_remote_database(remote_host, remote_pass)
    log.debug("Connected to database")

    log.info("Starting Chat Server:\t{}:{}".format(host, chat_port))
    chat_service = Chatbot(db_)
#    Sock_Server(host, chat_port, chat_service)
    server = flasker.FlaskServer(host, chat_port, chat_service)
    log.debug("started sock server")

    log.info("Starting Tensorflow Server:\t{}:{}".format(host, tf_port))
    TF_Server(host, tf_port)
    log.debug("TF started")

    EOF = "Everything Checks out"
    log.info(EOF)
    #sys.exit(EOF)

if __name__ == '__main__':
    try:
        main()
    except:
        log.error("and thats okay too.")
