#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

__author__ = 'lannocc'


import ag.logging as log
log.set(log.DEBUG)

from flask import Flask, request
flask = Flask(__name__)

from ag.tf_curses.server import chatservice

@flask.route('/')
def interface():
    #return "you got the web interface"
    html = '<html><body><form action="/talk" method="GET"><input type="text" name="text"><input type="submit"></form></body></html>'
    return html

@flask.route('/talk', methods=['GET', 'POST'])
def talk():
    text = request.args.get('text')
    #log.debug("you said: ", text)
    log.debug("talk", text=text, chatservice=chatservice)

    if chatservice is not None:
        try:
            response = chatservice.talk(text)
            log.info("server says: ", response)
        except:
            log.error()
    else:
        return "FlaskServer is working and your message received, but no chatbot service was provided";




def flaskytalkyrun(server=None):
    log.info("flaskytalkyrun", server=server)
    global chatservice
    chatservice = server
    if server is not None:
        flask.run(host=server.host, port=server.port, threaded=True)
    else:
        flask.run()



class FlaskChat(object):

    def __init__(self, host='0.0.0.0', port=5000, service=None):
        self.host = host
        self.port = port
        self.service = service

    def run(self):
        flaskytalkyrun(self)

    def talk(self, text):
        if self.service is not None:
            return self.service.talk(text)
        else:
            return "blah blah blah"


#    @flask.route('/foo')

if __name__ == "__main__":
    import ag.tf_curses.database.database_interface as db
    dictionary = db.Database('10.42.0.42', 6379, db=0)
    rev_dictionary = db.Database('10.42.0.42', 6379, db=1)
    database = [dictionary, rev_dictionary]

    import ag.tf_curses.chatbot.chatbot as chatbot
    service = chatbot.tf_chatbot(database)

    FlaskChat(service=service).run()


