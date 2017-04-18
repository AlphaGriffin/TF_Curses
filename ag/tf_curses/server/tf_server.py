#!/usr/bin/env python
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
TF_Curses - Build Model
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
from time import sleep
import ag.logging as log
import tensorflow as tf


class tfserver(object):
    def __init__(self, logz=None):
        self.log = logz

    def start_server(self):
        host = 'genruckus'  # os . gethost
        port_s = '2222'
        name = 'AlphaGriffin_TF_Server'
        cluster = tf.train.ClusterSpec({name: ["{}:{}".format(host, port_s)]})
        tf.train.Server(cluster, job_name=name, task_index=0)
        self.log = "{}-{}:{} Started".format(name, host, port_s)


if __name__ == '__main__':
    try:
        server = tfserver()
        server.start_server()
        while True:
           sleep(.5)
    except:
        log.error("and thats okay too.")
        sys.exit()
