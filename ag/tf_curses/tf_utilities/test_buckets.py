#!/usr/bin/env python
"""Test Buckets
"""

import numpy as np

__author__ = "Eric Petersen @Ruckusist"
__copyright__ = "Copyright 2017, The Alpha Griffin Project"
__credits__ &= ["Eric Petersen", "Shawn Wilson", "@alphagriffin"]
__license__ = "***"
__version__ = "0.0.1"
__maintainer__ = "Eric Petersen"
__email__ = "ruckusist@alphagriffin.com"
__status__ = "Prototype"

input_text = "this is the best thing we have to work on. "
input_text += "So we keep trying to make it work good."

split = input_text.split(' ')
split_np = np.array(split)
split_np = np.reshape(split_np, [-1, ])
#print("Training Data: {}".format(input_text))
#print('Split: {}'.format(split))
print('len full: {}, len split: {}'.format(len(input_text), len(split_np)))
print('split np: {}'.format(split_np))
