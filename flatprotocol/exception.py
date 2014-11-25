# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

class FlatProtocolException(Exception):
    pass

class UnsupportedKWargs(FlatProtocolException):
    def __init__(self, arg):
        self.arg = arg
        FlatProtocolException.__init__(self, arg)


