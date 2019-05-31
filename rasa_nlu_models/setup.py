#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rasa_nlu_models'],
    package_dir={'rasa_nlu_models':'ros/src/rasa_nlu_models'}
)

setup(**d)
