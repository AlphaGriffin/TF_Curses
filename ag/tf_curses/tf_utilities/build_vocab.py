#!/usr/bin/env python
"""The TF_Curses Project | alphagriffin 2017.

# tf_utilities/build_vocab.py

Create a dataset from a text document. It needs, vocab_size,
id2words, word2ids.
: Notes taken from JinTian, https://github.com/jinfagang.
"""

import os
import sys
import numpy as np
import nltk
from collections import Counter

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen",
               "Shawn Wilson",
               "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"


class Vocabulary(object):
    """Simple vocabulary wrapper."""
    def __init__(self):
        self.word2idx = {}
        self.idx2word = {}
        self.idx = 0

    def add_word(self, word):
        if not word in self.word2idx:
            self.word2idx[word] = self.idx
            self.idx2word[self.idx] = word
            self.idx += 1

    def __call__(self, word):
        if not word in self.word2idx:
            return self.word2idx['<unk>']
        return self.word2idx[word]

    def __len__(self):
        return len(self.word2idx)


def vocab_factory(text, threshold):
    """Build a simple vocabulary wrapper."""
    counter = Counter()

    for i, word in enumerate(text):
        tokens = nltk.tokenize.word_tokenize(word.lower())
        counter.update(tokens)

        if i+1 % 1000 == 0:
            print("[{}/{}] Tokenized the captions.".format(
                i, len(text)
                ))

    # If the word frequency is less than 'threshold', then the word is discarded.
    words = [word for word, cnt in counter.items() if cnt >= threshold]

    # Creates a vocab wrapper and add some special tokens.
    vocab = Vocabulary()
    vocab.add_word('<unk>')
    vocab.add_word('<pad>')
    vocab.add_word('<start>')
    vocab.add_word('<end>')


    # Adds the words to the vocabulary.
    for i, word in enumerate(words):
        vocab.add_word(word)
    return vocab

def main():
    """Test Vocabulary building function."""
    test = "going going back back to cali cali"
    test = test.split(' ')
    my_vocab = vocab_factory(test, threshold=2)
    print(len(my_vocab))
    for i in my_vocab.word2idx:
        print("Word {}: {}".format(i, my_vocab.idx2word[i]))


if __name__ == '__main__':
    os.system('clear')
    try:
        if main():
            sys.exit('All Passed | Alphagriffin.com')

    except Exception as e:
        sys.exit('Failed: {}\n\nFailed: Alphagriffin.com'.format(e))
