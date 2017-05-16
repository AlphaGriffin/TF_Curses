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
import ag.tf_curses.server.flask_server as flask_talker
log.set(log.WARN)


class Options(object):
    def __init__(self):
        self.host = "localhost"
        self.remote_host = 'agserver'
        self.remote_pass = 'dummypass'
        self.chat_port = 12345
        self.tf_port = 2222
        self.redis_port = 6379
        self.flask_port = 5000

class TF_Curses(object):
    def __init__(self, options):
        self.running = True
        self.options = options
        self.errors = []
        self.working_panels = []
        self.cur = 0
        self.menu = ["TF_Server",
                     "Database",
                     "Chatbot",
                     "Web_Server",
                     "Chess",
                     "Error_Log"]

    @property
    def is_running(self):
        return self.running

    def start_frontend(self, frame='curses'):
        pid = os.getpid()
        msg = "AlphaGriffin TF_Curses | "
        msg += "Start Time: {} | ".format(datetime.now().isoformat(timespec='minutes'))
        msg += "PID: {}".format(pid)
        if frame is 'curses':
            self.frontend = Curses()
            self.frontend.main_screen()
            msg_len = self.frontend.screen_w - 3
            if len(msg) > msg_len:
                msg = msg[:msg_len]
            self.frontend.header[0].addstr(1, 1, msg)
            #self.frontend.header[0].refresh()

    def start_backend(self): pass

    def Web_Server(self):
        try:
            self.webserver = flask_talker.FlaskChat()
            Thread(target=self.webserver.run).start()
            self.working_panels[self.cur][0].addstr(5, 5, "Service Running: {}".format(self.menu[self.cur]))
        except:
            msg = "Service Failed: {}".format(self.menu[self.cur])
            self.working_panels[self.cur][0].addstr(5, 5, msg)
            #self.working_panels[self.cur][0].addstr(5, 5, sys.exc_info()[0])
        pass

    def Chess(self):
        class ChessGame(): pass
        chessgame = ChessGame()
        msg = "AG_{}".format(self.menu[self.cur])
        self.working_panels[self.cur][0].addstr(1, 5, msg)
        # get window size
        y, x = self.working_panels[self.cur][0].getmaxyx()
        if y < 14 or x < 12:
            info = "x = {}, y = {}".format(x, y)
            self.working_panels[self.cur][0].addstr(2, 4, info)
            info = "Screen too small to display board"
            self.working_panels[self.cur][0].addstr(3, 4, info)
            return
        bsx = board_start_x = 3
        bsy = board_start_y = 3
        n = 8
        colors = "WB"
        board = [[colors[(i+j+n%2+1) % 2] for i in range(n)] for j in range(n)]
        positions = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for index, row in reversed(list(enumerate(board))):
            test_msg = "{}: ".format(index+1)
            self.working_panels[self.cur][0].addstr(bsy, bsx, test_msg)
            bsx += 3
            for this, square in enumerate(row):
                if square is 'W':
                    #row[this] = u'\u2588'
                    row[this] = 'W'
                    self.working_panels[self.cur][0].addstr(bsy, bsx, row[this], self.frontend.chess_white)
                elif square is 'B':
                    # row[this] = u'\u2588'
                    row[this] = 'B'
                    self.working_panels[self.cur][0].addstr(bsy, bsx, row[this], self.frontend.chess_black)
                else:
                    self.working_panels[self.cur][0].addstr(bsy, bsx, '')
                bsx += 1
            bsy += 1
            bsx = 3
        self.working_panels[self.cur][0].addstr(bsy, bsx, "#: ")
        bsx += 3
        for index, element in enumerate(positions):
            self.working_panels[self.cur][0].addstr(bsy, bsx, "{}".format(element))
            bsx += 1
        pass

    def Error_Log(self):
        msg = "Service: {} : Testing".format(self.menu[self.cur])
        msg += u"\u2588"
        self.working_panels[self.cur][0].addstr(1, 3, msg)
        y, x = self.working_panels[self.cur][0].getmaxyx()
        max_print = y-4
        index = 3
        # this is TOP DOWN
        #for count, j in enumerate(self.errors[-max_print:]):
        #    msg = "E:{0:3d} | {1}".format(len(self.errors) - count, j)
        #    self.working_panels[self.cur][0].addstr(index, 3, msg[:x-4])
        #    index += 1
        # this is Bottom UP
        for count, j in reversed(list(enumerate(self.errors[-max_print:]))):
            msg = "E:{0:3d} | {1}".format(len(self.errors) - count, j)
            self.working_panels[self.cur][0].addstr(index, 3, msg[:x-4])
            index += 1
        pass

    def Chatbot(self):
        msg = "Starting Service: {}".format(self.menu[self.cur])
        self.working_panels[self.cur][0].addstr(5, 5, msg)
        service = chatbot.tf_chatbot(self.database)
        host = self.options.host
        port = self.options.chat_port
        server = serv.Sock_Server(host, port, service)
        try:
            Thread(target=server.start_server).start()
            self.frontend.redraw_window(self.working_panels[self.cur])
            msg = "Service Running: {}".format(self.menu[self.cur])
            self.working_panels[self.cur][0].addstr(4, 3, msg)
            msg = "Use the AlphaGriffin Chat CLient @:".format()
            self.working_panels[self.cur][0].addstr(5, 3, msg)
            msg = "| {}:{} |".format(host, port)
            self.working_panels[self.cur][0].addstr(6, 3, msg, self.frontend.color_gb)
        except:
            msg = "Service Failed: {}".format(self.menu[self.cur])
            self.working_panels[self.cur][0].addstr(5, 5, msg)

    def Database(self):
        msg = "Starting Service: {}".format(self.menu[self.cur])
        self.working_panels[self.cur][0].addstr(5, 5, msg)
        h = self.options.remote_host
        p = self.options.redis_port
        dictionary = db.Database(h, p, db=0)
        rev_dictionary = db.Database(h, p, db=1)
        database = [dictionary, rev_dictionary]
        self.working_panels[self.cur][0].addstr(5, 5, msg)
        self.database = database
        msg = "Service Running: {}".format(self.menu[self.cur])
        self.working_panels[self.cur][0].addstr(5, 5, msg)
        return True

    def TF_Server(self):
        self.working_panels[self.cur][0].addstr(5, 5, "Starting Service: {}".format(self.menu[self.cur]))
        try:
            self.tfserver = tf_server.tfserver()
            Thread(target=self.tfserver.start_server).start()
            self.working_panels[self.cur][0].addstr(5, 5, "Service Running: {}".format(self.menu[self.cur]))
        except:
            msg = "Service Failed: {}".format(self.menu[self.cur])
            self.working_panels[self.cur][0].addstr(5, 5, msg)

    def main_loop(self):
        self.frontend.refresh()
        keypress = 0
        try:
            keypress = self.frontend.get_input()
        except:
            keypress = 0
            pass
        try:
            if keypress > 0:
                # self.errors.append(("keypress: ", keypress))
                self.decider(keypress)
        except:
            self.errors.append(("cmd", keypress))
            self.string_decider(keypress)
        ###
        # TODO: do other stuff
        ###

    def string_decider(self, string):
        if 'stop' in string:
            self.working_panels[self.cur][0].addstr(5, 5, "Stoping Service: {}".format(self.menu[self.cur]))
        else:
            self.working_panels[self.cur][0].addstr(1, 1, string)
        self.selector()

    def decider(self, keypress):
        # log.info("got this {} type {}".format(keypress, type(keypress)))
        # main decider functionality!
        try:
            if keypress is 113 or keypress is 1:
                command_text = """Exit"""
                self.errors.append(command_text)
                self.running = False
                pass
            elif keypress == 10:
                enter = self.menu[self.cur]
                command_text = """Enter"""
                self.errors.append(command_text)
                #self.working_panels[self.cur][0].addstr(4,5,"Attempting Service: {}".format(self.menu[self.cur]))
                # FIXME: DONT USE EVAL... WOW.!
                eval("self.{}()".format(enter))
                pass
            elif keypress == 9:
                command_text = """Tab"""
                if self.frontend.screen_mode:
                    self.frontend.screen_mode = False
                self.selector()
                pass
            elif keypress == 258:
                command_text = """scroll_up"""
                self.working_panels[self.cur][0].scroll(-1)
                self.frontend
                pass
            elif keypress == 259:
                command_text = """scroll_down"""
                self.errors.append(command_text)
                self.working_panels[self.cur][0].scroll(1)
                pass
            elif keypress == 338:
                command_text = """Page Down"""
                self.errors.append(command_text)
                if self.cur < len(self.menu) - 1:
                    self.cur += 1
                else:
                    self.cur = 0
                self.selector()
                pass
            elif keypress == 339:
                command_text = """Page Up"""
                self.errors.append(command_text)
                if self.cur > 0:
                    self.cur -= 1
                else:
                    self.cur = len(self.menu)-1
                self.selector()
                pass
            else:
                self.errors.append("""Unknown {}""".format(keypress))
                # log.error('Unknown Connand Function')
                pass
        finally:
            pass

    def selector(self):
        self.frontend.redraw_window(self.frontend.winleft)
        for index, item in enumerate(self.menu):
            if self.cur == index:
                self.frontend.winleft[0].addstr(index+1, 1, item, self.frontend.color_rw)
            else:
                self.frontend.winleft[0].addstr(index+1, 1, item, self.frontend.color_cb)
        self.working_panels[self.cur][1].top()
        if self.frontend.screen_mode:
            options = ["|q| to quit   |Tab| switch Mode   |enter| to start service", "|pgUp| change menu |pgDn| change menu"]
            self.frontend.redraw_window(self.frontend.debug)
            self.frontend.debug[0].addstr(1, 1, options[0], self.frontend.color_gb)
            self.frontend.debug[0].addstr(2, 1, options[1], self.frontend.color_gb)
        else:
            options = ["|q| to quit   |Tab| switch Mode", "|enter| submit   |'stop'| to kill service"]
            self.frontend.redraw_window(self.frontend.debug)
            self.frontend.debug[0].addstr(1, 1, options[0], self.frontend.color_gb)
            self.frontend.debug[0].addstr(2, 1, options[1], self.frontend.color_gb)

    def working_panel(self):
        # this is only run 1 time during setup
        for index, item in enumerate(self.menu):
            self.working_panels.append(self.frontend.make_panel(self.frontend.winright_dims, item, True))

    def main(self):
        self.start_frontend()
        self.start_backend()
        self.working_panel()
        self.selector()
        while self.is_running:
            time.sleep(.05)
            self.main_loop()
        self.exit_safely()

    def exit_safely(self, msg=None):
        try:
            self.frontend.end_safely()
            # DEPRICATED
            #for i in self.errors:
            #    print("Errors: {}".format(i))
            sys.exit("Supported by Alphagriffin.com")
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
