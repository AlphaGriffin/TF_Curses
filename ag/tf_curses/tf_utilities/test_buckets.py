#!/usr/bin/env python
"""Test Buckets.

This should serve the most basic functionality of a bucket
based lstm system. With the least amount of effort placed
on the actual chat function and more on the output of a
single message.
"""

import os
import sys
import numpy as np
import redis
import yaml

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ = ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"


class Database_(object):
    """A Copy and paste hack of database interface."""

    def __init__(self, options, host='192.168.99.225', pass_='dummypass', db=0):
        """Testing functionality."""
        self.options = options
        self.database = redis.Redis(
            host=host,
            password=pass_,
            db=db
        )

    def write_data(self, key, value):
        """Testing functionality."""
        self.database.set(key, value)
        return True

    def read_data(self, key):
        """Testing functionality."""
        try:
            value = self.database.get(key).decode('UTF-8')
        except:
            try:
                value = self.database.get(key)
            except Exception as e:
                print("Damnit on the reverse lookup!")
                value = 'unk'
        return value


class Options(object):
    """OH OH DO a yaml file!"""

    def __init__(self, data_path):
        """OH OH DO a yaml file!"""
        config = self.load_options(data_path)
        for i in config:
            setattr(self, '{}'.format(i), '{}'.format(config[i]))

    def load_options(self, data_path):
        """COOL! a yaml file."""
        try:
            with open(data_path, 'r') as config:
                new_config = yaml.load(config)
            return new_config
        except Exception as e:
            print("burn {}".format(e))


class DataPrep(object):
    """Handle data translations."""
    def __init__(self, options):
        """Take as little as possible as user input.

        Use a config.
        """
        self.options = options
        self.input_source = os.path.join(self.options.input_path)
        self.translation_source = os.path.join(self.options.translation_path)
        # Special vocabulary symbols - we always put them at the start.
        self._PAD = b"_PAD"
        self._GO = b"_GO"
        self._EOS = b"_EOS"
        self._UNK = b"_UNK"
        self._START_VOCAB = [self._PAD, self._GO, self._EOS, self._UNK]

        self.PAD_ID = 0
        self.GO_ID = 1
        self.EOS_ID = 2
        self.UNK_ID = 3
        self.buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]
        self.max_size = None

        # self.dataset = self.prep_buckets()

    def prep_buckets(self):
        """Prep the buckets."""
        data_set = [[] for _ in self.buckets]
        with open(self.input_source, 'r', encoding='UTF-8') as input_:
            with open(
                self.translation_source, 'r', encoding='UTF-8'
                ) as translation_:
                counter = 0
                source = input_.readline()
                target = translation_.readline()
                while source and target and (
                        not self.max_size or counter < self.max_size):
                    counter += 1
                    if counter % 100000 == 0:
                        print("dang this is a lot of data... hold on.")
                        sys.stdout.flush()
                    source_ids = [int(x) for x in source.split()]
                    target_ids = [int(x) for x in target.split()]
                    # target_ids.append(self.EOS_ID)
                    for bucket_id, element in enumerate(self.buckets):
                        source_size, target_size = element
                        if len(
                            source_ids
                            ) < source_size and len(
                                target_ids
                                ) < target_size:
                            data_set[bucket_id].append(
                                [source_ids, target_ids])
                            break
                        # reload
                        source = input_.readline()
                        target = translation_.readline()
        return data_set


class Network(object):
    """A test framework."""
    def __init__(self, options):
        self.options = options

    @property
    def save_dir(self):
        """Return Necessary option for this class."""
        return self.options.model_save_dir

    @property
    def model_name(self):
        """Return Necessary option for this class."""
        return self.options.model_save_name


class App(object):
    """A test framework."""
    def __init__(self, options):
        """Take all the initalizers."""
        self.network = Network(options)
        self.dataset = DataPrep(options)
        self.database0 = Database_(options, db=0)
        self.database1 = Database_(options, db=1)
        self.options = options
        self.test = 0

    def main(self):
        """Run main app tests."""
        self.test = 1
        return True




def main():
    """For testing purpose."""
    config_path = os.path.join(os.getcwd(), 'config.yaml')
    config = Options(config_path)
    app = App(config)
    if app.main():
        sys.exit('All Good. | Alphagriffin.com (c)2017')
    return True


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("and thats okay too.")
        sys.exit(e)
