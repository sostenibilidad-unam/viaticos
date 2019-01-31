# -*- coding: utf-8 -*-
from distutils.core import setup
import py2exe, sys

sys.argv.append('py2exe')

setup(
    windows=[
            {
                "script": "viaticos.py"
            }
        ],


    options={
               "py2exe":{
                       "unbuffered": True,
                       "optimize": 2,
                       "includes":["PySide2.QtCore","PySide2.QtGui", "xml", "xlsxwriter"]
               }
       },

)
