"""
This is a setup.py script generated by py2applet

Usage:
    python py2app_setup.py py2app
"""
#import ez_setup
#ez_setup.use_setuptools()

import sys
from setuptools import setup

mainscript = 'f-engrave.py'
version = "1.64"
url = "https://github.com/stephenhouser/f-engrave"

if sys.platform == 'darwin':
     extra_options = dict(
         setup_requires=['py2app'],
         # Cross-platform applications generally expect sys.argv to
         # be used for opening files.
         options=dict(py2app = {
            'argv_emulation': False,
            'argv_inject': ['--fontdir', '/Library/Fonts', '--defdir', '~/Documents'],
            'iconfile': 'fengrave.icns',
            'resources': ['TTF2CXF_STREAM/ttf2cxf_stream'],
            #'semi_standalone': True,
            }),
     )
elif sys.platform == 'win32':
    extra_options=dict(
        setup_requires=['py2exe'],
        options=dict(py2exe={
            'compressed': 0,
            'optimize': 0
        }),
        zipfile=None,
        console=[{'script':'f-engrave.py', 'icon_resources':[(0,'fengrave.ico'),(0,'fengrave.ico')]}]
     )
else:
     extra_options = dict(
         # Normally unix-like platforms will use "setup.py install"
         # and install the main script as such
         scripts=[mainscript],
     )

setup(
    #name="F-Engrave",
    app=[mainscript],
    version=version,
    url=url,
    **extra_options
    )
