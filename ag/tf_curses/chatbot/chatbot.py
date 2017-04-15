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

import os, sys, time
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '5'
from datetime import datetime
import tensorflow as tf
import numpy as np
import ag.logging as log
log.set(5)


class chatbot(object):
    def __init__(self, database, user=None, Session=None):
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
    def __init__(self, database, init=False, user=None, Session=None):
        self.__service_name__ = 'Chatbot'
        self.dictionary = database[0]
        self.rev_dictionary = database[1]
        self.conversation = []
        self.sess = None
        self.model_loaded = False
        self.params = None
        self.user = user
        self.Session = Session

    @property
    def servcie_name(self):
        return self.__service_name__



    def main(self):
        log.info("beginning chabot test")
        if self.load_tf_model():
            if self.load_model_params():
                if self.params.test is "okay":
                    log.info("Params Loaded.")
                    pass

        input_test = "This is cool"
        test =  self.talk(input_test)
        # log.debug("Return Message: {}".format(test))
        if test:
            log.info("You: {}\nMe: {}".format(input_test, test))
            return True
        return False

    def start_tf_session(self):
        if self.sess:
            self.sess.close()
        self.session = tf.InteractiveSession()
        pass

    def stop_tf_session(self):
        if self.sess:
            self.sess.close()
        pass

    def stop_converstion(self):
        pass

    def load_tf_model(self, folder=None):
        if folder is None: folder = "/pub/models"
        log.info("Loading Model: {}".format("Model_Name"))
        if self.sess:
            self.sess.close()
        try:
            self.sess = tf.InteractiveSession()
            checkpoint_file = tf.train.latest_checkpoint(folder)
            log.info("trying: {}".format(checkpoint_file))
            new_saver = tf.train.import_meta_graph(checkpoint_file + ".meta")
            log.debug("loading modelfile {}".format(folder))
            new_saver.restore(self.sess, checkpoint_file)
            log.info("model successfully Loaded: {}".format(folder))
            self.model_loaded = True
        except Exception as e:
            log.warn("This folder failed to produce a model {}\n{}".format(folder, e))
        return True

    def load_model_params(self):
        log.info("Loading Model Params")
        class params(object): pass
        params.list_all_ops = [n.name for n in tf.get_default_graph().as_graph_def().node]
        log.debug("Num ops in model: {}".format(len(params.list_all_ops)))
        params.final_layer = tf.get_collection_ref('final_layer')[0]
        #log.debug("Found Final Layer: {}".format(params.final_layer))
        #params.encoder = tf.get_collection_ref('encoder')[0]
        #log.debug("Found encoder op: {}".format(params.encoder))
        #params.encoder = tf.get_collection_ref('decoder')[0]
        #log.debug("Found decoder op: {}".format(params.decoder))
        params.input_tensor = tf.get_collection_ref('input_word')[0]
        #log.debug("Found input tensor: {}".format(params.input_tensor))
        params.input_label = tf.get_collection_ref('input_label')[0]
        #log.debug("Found input label: {}".format(params.input_label))
        params.global_step = tf.get_collection_ref('global_step')[0]
        #log.debug("Found global_step: {}".format(params.global_step))
        params.learn_rate = tf.get_collection_ref('learn_rate')[0]
        #log.debug("Found learn_rate: {}".format(params.learn_rate))
        params.correct_pred = tf.get_collection_ref('correct_pred')[0]
        #log.debug("Found correct_pred op: {}".format(params.correct_pred))
        params.accuracy = tf.get_collection_ref('accuracy')[0]
        #log.debug("Found accuracy op: {}".format(params.accuracy))
        params.cost = tf.get_collection_ref('cost')[0]
        #log.debug("Found cost op: {}".format(params.cost))
        params.optimizer = tf.get_collection_ref('optimizer')[0]
        #log.debug("Found optimizer op: {}".format(params.optimizer))
        params.test = "okay"
        self.params = params
        return True

    def get_word(self, symbols_in_keys):
        resp_len = 3
        keys = np.reshape(np.array(symbols_in_keys[-resp_len:]), [-1, resp_len, 1])
        # x = tf.placeholder("float", [None, 3, 1])
        feed_dict = {self.params.input_tensor: keys}
        onehot_pred = self.sess.run(self.params.final_layer, feed_dict=feed_dict)

        thing = tf.argmax(onehot_pred, 1)
        #log.debug("{}".format(thing))
        ohpi = self.sess.run(thing)
        log.debug("{}".format(ohpi))
        # onehot_pred_index = int().eval(session=self.sess))
        new_word = self.rev_dictionary.read_data(ohpi)
        return new_word

    def test_reponse(self, input_string):
        log.info("Starting reponse from input: {}".format(input_string))
        responding = True
        response = ""
        symbols_in_keys = []
        while responding:
            try:
                log.debug("responding")
                words = input_string.split(' ')
                for i in range(len(words)):
                    symbols_in_keys.append(self.dictionary.read_data(str(words[i])))

                new_word = self.get_word(symbols_in_keys)
                log.debug("got a new word: {}".format(new_word))
                symbols_in_keys.append(self.dictionary.read_data(new_word))
                response = new_word

            except Exception as e:
                log.fatal("Errors!!!\n{}".format(e))
                sys.exit(e)

            responding = False

        return response

    def respond(self, input_string):
        log.info("Starting reponse from input: {}".format(input_string))

        # x = tf.placeholder(tf.float32, [-1, len_input, 1])
        responding = True
        response = ""
        while responding:
            words = input_string.split(' ')
            len_input = len(input_string)
            if len(words) != len_input:
                log.debug("Still getting more words {} != {}".format(len(words), len_input))
                continue
            try:
                # this is our input string
                for i in range(len_input):
                    symbols_in_keys.append(self.database.read_data(str(words[i])))

                new_word = self.get_word(symbols_in_keys)
                log.debug("got a new word: {}".format(new_word))
                symbols_in_keys.append(self.database.read_data(new_word))
            except:
                log.warn("Failing to find a word")
                pass
            responding = False
        log.info("{} :\n\t{}".format(input_string, response))
        return response

    def talk(self, msg):
        input_string = msg.split(' ')
        resp_len = len(input_string)
        symbols_in_keys = []
        response = ""
        if resp_len >= 10:
            resp_len = 10
        for i in range(resp_len):
            symbols_in_keys.append(self.dictionary.read_data(str(input_string[i])))

        for i in range(resp_len):
            log.debug("responding")
            # get a new word
            new_word = self.get_word(symbols_in_keys)
            # add that word to the continueing context
            symbols_in_keys.append(self.dictionary.read_data(new_word))
            # add the word to the output
            response += "{} ".format(new_word)
        return response

if __name__ == '__main__':
    import database_interface as db
    log.info("Starting the Chatbot Testing")
    log.debug("starting redis")
    dict = db.Database(db=0)
    rev_dict = db.Database(db=1)
    database = [dict, rev_dict]
    try:
        app = tf_chatbot(database)
        if app.main():
           sys.exit("Everything checks out.")
    except Exception as e:
        log.error("and thats okay too.")
        sys.exit(e)
