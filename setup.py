#!/usr/bin/env python
#
# Copyright (C) 2017 Alpha Griffin
# @%@~LICENSE~@%@

"""
TF_Curses
Alphagriffin.com
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""


"""
AlphaGriffin setuptools build script.

@author Ruckusist

@see    https://packaging.python.org/en/latest/distributing.html
@see    https://github.com/pypa/sampleproject

Some of this script logic also taken from:
        https://github.com/google/protobuf
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

if __name__ == '__main__':

    setup(

        name='TF_Curses',
        version='0.0.1',
        license='AG',  # FIXME

        namespace_packages=['ag'],  # home for Alpha Griffin libraries
        packages=find_packages(exclude=['tests']),

        author='Ruckusist @ Alpha Griffin',
        author_email='ruckusist@alphagriffin.com',

        description='Tensorflow Training User Interface for Distributed Networks',
        long_description=open('README.rst').read(),
        url='http://github.com ruckusist.tf_curses',

        # @see https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            'Development Status :: 3 - Alpha',
            "Environment :: Console",
            "Environment :: Console :: Curses",
            'Intended Audience :: Developers',
            "Operating System :: POSIX",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            'Natural Language :: English',
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.2",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: Implementation :: PyPy",
            'Topic :: System :: Installation/Setup',
            'Topic :: Utilities'
        ],

        # space-separated list of keywords
        keywords='alphagriffin tensorflow utilities curses ui user interface text urwid',
        platforms="unix-like",

        # run-time dependencies
        install_requires=['setuptools',
                          'twisted',
                          'tornado',
                          'urwid',
                          # 'ag.logging',
                          # 'curses',
                          ],  # setuptools here for example only (it's implied)

        extras_require={
        },

        package_data={
        },

        data_files=[],

        entry_points={
            'console_scripts': [
                'tf_curses = ag.tf_curses.__main__'
            ]
        },
    )

