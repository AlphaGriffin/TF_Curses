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
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from datetime import datetime
from time import sleep
from threading import Thread
import ag.logging as log
import ag.tf_curses.server.basic_server as serv
import ag.tf_curses.chatbot.chatbot as chatbot
import ag.tf_curses.server.tf_server as tf_server
import ag.tf_curses.database.database_interface as db
from ag.tf_curses.frontend.curses_frontend import Window as Curses

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

def old_main():
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
    Sock_Server(host, chat_port, chat_service)
    log.debug("started sock server")

    log.info("Starting Tensorflow Server:\t{}:{}".format(host, tf_port))
    TF_Server(host, tf_port)
    log.debug("TF started")

    EOF = "Everything Checks out"
    log.info(EOF)
    #sys.exit(EOF)

class Options(object):
    def __init__(self):
        self.host = "localhost"
        self.remote_host = 'agserver'
        self.remote_pass = 'dummypass'
        self.chat_port = 12345
        self.tf_port = 2222
        self.redis_port = 6379

class TF_Curses(object):
    def __init__(self, options):
        self.running = True
        self.options = options

    @property
    def is_running(self):
        return self.running

    def start_frontend(self, frame='curses'):
        log.debug("Starting Frontend")
        if frame is 'curses':
            self.frontend = Curses()
            # TODO: setup main window
            self.frontend.screen.addstr(4,4, "press q to exit.",
                                        self.frontend.color_rw)

    def start_backend(self):
        log.debug("Starting Backend")

    def main_loop(self):
        self.frontend.refresh()
        keypress = 0
        try:
            keypress = self.frontend.get_input()
        except:
            keypress = 0
            pass
        if keypress is not 0:
            self.decider(keypress)
        ###
        # TODO: do other stuff
        ###

    def decider(self, keypress):
        log.info("got this {} type {}".format(keypress, type(keypress)))
        # main decider functionality!
        try:
            if keypress is 113 or keypress is 1 or keypress is 27:
                command_text = """Exit Command:
                q command pressed... also want:
                ctrl+q, ctrl+x, ctrl+esc
                """
                log.debug(command_text)
                self.running = False
                pass
            elif input == '':
                pass
            else:
                log.error('Unknown Connand Function')
                pass
        finally:
            pass

    def main(self):
        self.start_frontend()
        self.start_backend()
        while self.is_running:
            self.main_loop()
        self.exit_safely()

    def exit_safely(self, msg=None):
        try:
            self.frontend.end_safely()
            sys.exit("Supported by Alphagriffin.com\n{}".format(msg))
        except Exception as e:
            sys.exit("Supported by Alphagriffin.com\n{}".format(e))

def main():
    # hoping to use an ini file here... this class will probably still parse that though
    options = Options()
    # TODO: this is still missing a command line arg parser!
    app = TF_Curses(options)
    try:
        app.main()
        os.system('clear')
    except KeyboardInterrupt:
        app.exit_safely()
        os.system('clear')
        pass

if __name__ == '__main__':
    try:
        main()
    except:
        log.error("and thats okay too.")