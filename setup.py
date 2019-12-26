#!/usr/bin/env python

# $Id: setup.py,v 1.1 2002/06/21 18:10:49 jgoerzen Exp $

import os
from distutils.core import setup, Command
from setuptools import setup, find_packages
import versionhelp


setup(name = "versionhelp",
      version = '0.2',
      description = 'Simple Universal Version Command',
      author = 'Kishore',
      author_email = 'prakis@gmail.com',
      url = 'https://versionhelp.com',
      license = 'Licensed under the MIT version ',      
      py_modules=['versionhelp'],
      entry_points={  'console_scripts': [ 'versionhelp = versionhelp:main' ]  }
)

#cmdclass = { 'test': TestCommand}

