#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

from flask import Flask, request
flask = Flask(__name__)

import ag.logging as log

log.set(log.DEBUG)


flaskservice = None

@flask.route('/', defaults={'path': ''})
@flask.route('/<path:path>')
def flaskytalky(path):
    text = request.path[1:]
    log.debug("you said: ", text)

    if flaskservice is not None:
        response = flaskservice.talk(text)
        log.info("server says: ", response)
    else:
        return "FlaskServer is working but no service was provided";


def flaskytalkyrun(server=None):
    if server is not None:
        flask.run(host=server.host, port=server.port, threaded=True)
    else:
        flask.run()



class FlaskServer(object):

    def __init__(self, host='0.0.0.0', port=12345, service=None):
        self.host = host
        self.port = port
        self.service = service

        flaskservice = service

    def run(self):
        flaskytalkyrun(self)

#    @flask.route('/foo')

if __name__ == "__main__":
    flaskytalkyrun()


