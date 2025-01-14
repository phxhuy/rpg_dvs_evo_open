#!/usr/bin/env python3

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['vikit_py'],
    package_dir={'': 'src'},
    install_requires=['rospkg', 'yaml'],
    )

setup(**d)