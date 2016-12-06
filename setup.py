#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of xlart.
# https://github.com/ayvazj/xlart

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016, James Ayvaz <james.ayvaz@gmail.com>

from setuptools import setup, find_packages
from xlart import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='xlart',
    version=__version__,
    description='Excel art generator',
    long_description='''
Excel art generator
''',
    keywords='excel pixel art',
    author='James Ayvaz',
    author_email='james.ayvaz@gmail.com',
    url='https://github.com/ayvazj/xlart',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=False,
    install_requires=[
        'openpyxl>=2.4.1',
        'Pillow>=3.4.2'
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'xlart=xlart.cli:main',
        ],
    },
)
