#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) 2013 Andreas Motl

import setuptools
from setuptools import setup, find_packages

setup(
    name="drupal-filemover",
    version="0.0.1",
    author="Andreas Motl",
    url="https://github.com/amotl/drupal-filemover",
    author_email="amo@netfrag.org",
    py_modules = ["drupal_filemover"],
    include_package_data=True,
    extras_require=dict(
        test=[
        ]
    ),
    install_requires=[
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'dfm-scan = drupal_filemover:scan',
            'dfm-move = drupal_filemover:move',
            'dfm-updatedb = drupal_filemover:updatedb',
        ],
    },
)
