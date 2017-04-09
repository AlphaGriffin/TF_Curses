# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
TF_Curses
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

import os
from datetime import datetime
import tensorflow as tf
import numpy as np



class chatbot(object):
    def __init__(self, user=None, Session=None):
        if user is None:
            user = 'Prof_Falken'
        self.current_user = user
        if Session is None:
            Session = 420
        self.current_sess = Session
        self.current_dialog = '{}-{}-dialog.txt'.format(Session, user)
        save_file = os.path.join(os.getcwd(), self.current_dialog)
        _ = self.concat("--$ Starting a conversation with {}".format(user))
        # start tensorflow
        # load model
        # test script with first word for + 1 word for greeting
        # all good boolean

    def talk(self, message):
        """private method"""
        # add the message to our compete conversation
        flags = self.chat_input(message)
        message = "$ {} |{}|: {}\n".format(self.current_user, datetime.now().isoformat(timespec='minutes'), message)
        Issues = []
        if flags:
            for i in flags:
                Issues.append(self.dealwith(i))
        conversation = self.concat(issues=Issues, message=message)
        current_thought = self.chat_output(conversation)
        chat = "{}\n{}".format(message, current_thought)
        return chat

    def chat_input(self, message):
        """Filters the chat for keywords. can you do it dynamically?"""
        flags = []
        if 'services' in message:
            flags.append(['services'])
        return flags

    def dealwith(self, flag):
        issues = []
        results = self.search(flag)
        if results:
            for key in results:
                value = self.load_data(key)
                issues.append([key, value])
            return issues
        else:
            key = str(flag)
            value = 'flag'
            self.store_data([key, value])
            issues.append([key, value])
            return issues

    def search(self, flag):
        result = 0
        return result

    def concat(self, message, issues=None):
        conversation = None
        with open(self.current_dialog, 'w', encoding='ascii') as current_text:
            current_text.write("{}\n".format(message))
            if issues:
                current_text.write("Current Issues: {}\n".format(issues))
        with open(self.current_dialog, 'r', encoding='ascii') as current_text:
            conversation = current_text.read()
        return conversation

    def store_data(self, data):
        # save to database
        x = [(data[0], data[1])]
        del x
        return True

    def load_data(self, key):
        # load data from database ...
        value = "key = {}".format(key)
        return key, value

    def chat_output(self, conversation):
        # log this instance

        # LOGICS ---
        # feel the tensors flow
        # conversation goes into TF and a message comes out!
        message = "{}".format(conversation[::1])
        message = "$ chatbot |{}|: {}\n".format(datetime.now().isoformat(timespec='minutes'), message)
        _ = self.concat(message)
        # /LOGICS --
        # given a return
        return message



class tf_chatbot(object):

    def __init__(self, init=False):
        self.conversation = []

    def start_tf_session(self):

        pass

    def stop_tf_session(self):

        pass

    def stop_converstion(self):

        pass

    def load_tf_model(self):

        pass


    def respond(self, input_string):
        len_input = len(input_string)
        responding = True
        response = ""
        while responding:
            words = input_string.split(' ')
            if len(words) != len_input:
                continue
            try:
                # this is our input string
                symbols_in_keys = [dictionary[str(words[i])] for i in range(len(words))]

                # for ??? attempts... to create a string.
                for i in range(32):
                    # words as np array
                    keys = np.reshape(np.array(symbols_in_keys), [-1, len_input, 1])
                    onehot_pred = session.run(pred, feed_dict={x: keys})
                    # get the argmax value which is the 1 hot encoded fully connected layer
                    # with the highest value being the # the correstponds with your answor
                    onehot_pred_index = int(tf.argmax(onehot_pred, 1).eval())
                    # and this is the word from the dict which is # to word not word to #
                    new_word = reverse_dictionary[onehot_pred_index]
                    # collect the new words in to a sentence in kind with the question.
                    response = "{} {}".format(response, new_word)
                    # possiably remoes that word from the index...
                    symbols_in_keys = symbols_in_keys[1:]
                    # add this word to the continuing senstence for continueing speech
                    symbols_in_keys.append(onehot_pred_index)
                responding = False

            except:
                log.warn("Failing to find a word")
                pass
        log.info("{} :\n\t{}".format(input_string, response))
        return response

