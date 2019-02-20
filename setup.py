#!/usr/bin/env python

import setuptools
from flat_kivy.__init__ import __version__

setuptools.setup(name='FlatKivy',
    version=__version__,
    description='A collection of experimental flat/material design widgets for Kivy.',
    author='Kovak',
    url='https://github.com/Kovak/FlatKivy',
    packages=setuptools.find_packages(),
    package_data = {'': [
        '*.kv',
        'data/*.kv',
        'data/font/*.ttf',
        'data/images/*.png',
        '*.json']},
    )