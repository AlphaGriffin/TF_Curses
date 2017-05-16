#!/usr/bin/env python
"""TF_Curses, Alphagriffin.com.
Eric Petersen @Ruckusist <eric.alphagriffin@gmail.com>
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

if __name__ == '__main__':
    # long_description breaks out of DIR installs!
    setup(

        name='TF_Curses',
        version='0.0.1',
        license='AG',  # FIXME

        namespace_packages=['ag'],  # home for Alpha Griffin libraries
        packages=find_packages(exclude=['tests']),

        author='Ruckusist @ Alpha Griffin',
        author_email='ruckusist@alphagriffin.com',

        description='Tensorflow User Interface for Distributed Networks',

        long_description=open('README.rst').read(),
        url='http://github.com/alphagriffin/tf_curses',

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
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: Implementation :: PyPy",
            'Topic :: System :: Installation/Setup',
            'Topic :: Utilities'
        ],

        # space-separated list of keywords
        keywords='alphagriffin tensorflow utilities curses ui user interface text',
        platforms="unix-like",

        # run-time dependencies
        # twisted is a threading program... will be upgraded to soon.
        # tf gpu is breaking on the server install
        install_requires=['setuptools',
                          'tensorflow',
                          'numpy',
                          'flask',
                          'redis',
                          'inflect',
                          ],  # setuptools here for example only (it's implied)

        extras_require={
        },

        package_data={
        },

        data_files=[],

        entry_points={
            'console_scripts': [
                'tf_curses = ag.tf_curses.__main__:main'
            ]
        },
    )
