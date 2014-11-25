# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


import os

CURRENT_PATH = os.path.normpath(os.path.dirname(os.path.relpath(__file__)))
files = os.listdir(CURRENT_PATH)
for _f in files:
    if _f.endswith('.py') and _f != '__init__.py':
        __import__('flatprotocol.templates.{0}'.format(_f[:-3]))

del os
del files
del CURRENT_PATH
