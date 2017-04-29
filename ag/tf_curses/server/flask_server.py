#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

__author__ = 'lannocc'


import ag.logging as log
log.set(log.DEBUG)

from flask import Flask, request
flask = Flask(__name__)

flaskservice = None

@flask.route('/')
def interface():
    #return "you got the web interface"
    html = '<html><body><form action="/talk" method="GET"><input type="text" name="text"><input type="submit"></form></body></html>'
    return html

@flask.route('/talk', methods=['GET', 'POST'])
def talk():
    text = request.args.get('text')
    log.debug("you said: ", text)

    if flaskservice is not None:
        response = flaskservice.talk(text)
        log.info("server says: ", response)
    else:
        return "FlaskServer is working and your message received, but no chatbot service was provided";




def flaskytalkyrun(server=None):
    if server is not None:
        flask.run(host=server.host, port=server.port, threaded=True)
    else:
        flask.run()



class FlaskChat(object):

    def __init__(self, host='0.0.0.0', port=5000, service=None):
        self.host = host
        self.port = port
        self.service = service

        flaskservice = service

    def run(self):
        flaskytalkyrun(self)

#    @flask.route('/foo')

if __name__ == "__main__":
    import ag.tf_curses.database.database_interface as db
    dictionary = db.Database('localhost', 6379, db=0)
    rev_dictionary = db.Database('localhost', 6379, db=1)
    database = [dictionary, rev_dictionary]

    import ag.tf_curses.chatbot.chatbot as chatbot
    service = chatbot.tf_chatbot(database)

    flaskytalkyrun(service)


