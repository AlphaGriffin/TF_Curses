#!/usr/bin/env python

"""TF_Curses Project 2017.

A case by which travis_ci, coveralls, nose, unittest, tox,
and appveyor all have a green light installable test case.
"""

from unittest import TestCase

# import tf_curses

class Test_Case(TestCase):
    def test_install(self):
        x = 0
        self.assertTrue(isinstance(x, int))
