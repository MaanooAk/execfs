#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'execfs',
    version = '1.0.0',

    description = 'The superior FUSE filesystem for exec on file open',
    author = 'Akritas Akritidis',
    author_email = 'akritasak@gmail.com',
    maintainer = 'Akritas Akritidis',
    maintainer_email = 'akritasak@gmail.com',
    license = 'MIT',
    url = 'http://github.com/MaanooAk/execfs',

    scripts = ["execfs"],
    install_requires = ['fusepy'],

    classifiers = [
        'Topic :: System :: Filesystems',
    ]
)
