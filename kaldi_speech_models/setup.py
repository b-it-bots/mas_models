#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['kaldi_speech_models'],
    package_dir={'kaldi_speech_models':'ros/src/kaldi_speech_models'}
)

setup(**d)
