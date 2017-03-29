#!/usr/bin/env python
"""This is an implementation of a basic sock sever.
The orginal idea for this is from:
http://danielhnyk.cz/simple-server-client-aplication-python-3/
"""
__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "Daniel Hnyk", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

import sys
from datetime import datetime
from threading import Thread
import socket
import os
import traceback
import ag.logging as log
log.set(5)


class Sock_Server(object):
    """A basic Socket Server"""
    def __init__(self, host, port, service=None):
        self.host = host
        self.hostport = port
        self.service = service

    def handle(self, input_string):
        """A String Parser / Decider"""
        log.debug(input_string)
        if input_string == 'services':
            if self.service:
                response = self.service.talk(input_string)
                return response
            else:
                return "No Services Running"
        if input_string == 'stop services':
            if self.service:
                return "Stoping Service - {}".format(str(self.service))
            else:
                return "No Services Running"
        if input_string == 'find /path/':
            return "fount /path/to/thing"
        else:
            x = self.service.talk(input_string)
            return x

    def client_thread(self, conn, ip, port, mbs=4096):
        """This is the manager of the input calls"""
        input_from_client_bytes = conn.recv(mbs)
        siz = sys.getsizeof(input_from_client_bytes)
        if siz >= mbs:
            log.info("The length of input is probably too long: {}".format(siz))

        # decode input and strip the end of line
        input_from_client = input_from_client_bytes.decode("utf8").rstrip()
        res = self.handle(input_from_client)
        log.info("Result of processing {} is: {}".format(input_from_client, res))

        vysl = res.encode("utf8")  # encode the result string
        conn.sendall(vysl)  # send it to client
        conn.close()  # close connection
        log.info('Connection ' + ip + ':' + port + " ended")

    def start_server(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # this is for easy starting/killing the app
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        log.info('Socket created')

        try:
            soc.bind(("127.0.0.1", 12345))
            log.info('Socket bind complete')
        except socket.error as msg:
            log.info('Bind failed. Error : ' + str(sys.exc_info()))
            sys.exit()
        soc.listen(10)
        log.info('Socket now listening')
        while True:
            conn, addr = soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            log.info("Connection Established - {}\n# -IP\t-{}:{}".format(datetime.now().isoformat(timespec='minutes'), ip, port))
            try:
                Thread(target=self.client_thread, args=(conn, ip, port)).start()
            except Exception as e:
                log.info("Terible error! {}".format(e))
                traceback.print_exc()
        soc.close()  # dont worry about it.


def main():
    pid = os.getpid()
    time = datetime.now().isoformat(timespec='minutes')
    host = "127.0.0.1"
    port = 12345
    mesg = "Starting Sock_Server\n\tTime: {}\n\tPID: {}\n\tServer- {}:{}".format(datetime.now().isoformat(timespec='minutes'), pid, host, port)
    log.info(mesg)
    server = Sock_Server(host, port, pid)
    Thread(target=server.start_server).start()
    log.info("Sock Server is up and running on port {}".format(port))

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log.info("and thats okay too.")
        log.error(e)
