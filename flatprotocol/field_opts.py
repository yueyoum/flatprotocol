# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from flatprotocol.exception import UnsupportedFieldOptions

__all__ = ['BaseFieldOptions',]



class BaseFieldOptions(object):
    SUPPORTED_OPTIONS = ['optional',]
    optional = False

    @classmethod
    def make_opts(cls, field, **kwargs):
        for k in kwargs:
            if k not in cls.SUPPORTED_OPTIONS:
                raise UnsupportedFieldOptions(k)

        for k in cls.SUPPORTED_OPTIONS:
            v = kwargs.get(k, None) or getattr(cls, k)
            setattr(field, k, v)

