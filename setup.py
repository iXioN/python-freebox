#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  setup.py
#  python-freebox
#  
#  Created by Antonin Lacombe on 2013-04-04.
#  Copyright 2013 Antonin Lacombe. All rights reserved.
# 

import sys
from setuptools import setup
from freebox import __version__

requirements = open('requirements.txt').readlines()

setup(name='freebox',
    version=__version__,
    license='LGPLv3',
    description='a freebox (French set-top box) python client and cli  management',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    keywords='freebox',
    author='Antonin Lacombe',
    author_email='antonin.lacombe@gmail.com',
    url='https://github.com/iXioN/python-freebox.git',
    packages=['freebox', ],
    entry_points={
        'console_scripts': ['freebox = freebox.freebox:main'],
    },
    #test_suite='python-freebox.tests.suite',
    install_requires=requirements,)
