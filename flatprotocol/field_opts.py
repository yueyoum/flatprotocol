# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

SUPPORTED_OPTIONS = ['optional', 'default',]

from flatprotocol.exception import UnsupportedKWargs

__all__ = ['FieldOptions', 'IntegerFieldOptions', 'FloatFieldOptions',
           'BinaryFieldOptions', 'ListFieldOptions']

class FieldOptions(object):
    optional = False

    @classmethod
    def make_opts(cls, **kwargs):
        for k in kwargs:
            if k not in SUPPORTED_OPTIONS:
                raise UnsupportedKWargs(k)

        opts = {}
        for k in SUPPORTED_OPTIONS:
            v = kwargs.get(k, None) or getattr(cls, k)
            opts[k] = v

        return opts


class IntegerFieldOptions(FieldOptions):
    default = 0

class FloatFieldOptions(FieldOptions):
    default = 0

class BinaryFieldOptions(FieldOptions):
    default = ""

class ListFieldOptions(FieldOptions):
    default = []


