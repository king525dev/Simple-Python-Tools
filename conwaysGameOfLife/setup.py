# setup.py
# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe
import sys

# This ensures that a console window is displayed for command-line programs
sys.argv.append('py2exe')

setup(
     name='ConwaysGameOfLife',
     version='1.0',
     description='Conway\'s Game of Life is a cellular automaton that is played on a 2D square grid.',
     author='king525dev',
     windows=['main.py'],  # replace with ['main.py'] for console app or windows=['main.py'] for GUI app
     options={
          'py2exe': {
               'packages': ['modules'],  # Include specific Python packages
               'includes': [], # Add extra modules if needed
               'excludes': [],  # Exclude modules not needed
               #'bundle_files': 1,   # bundle everything into a single executable
               #'compressed': True
          }
     },
     zipfile=None  # put the library files inside the exe
)