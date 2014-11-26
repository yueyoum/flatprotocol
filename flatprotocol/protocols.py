# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from fields import *


__all__ = ['Protocol',]


class ProtocolMeta(type):
    def __new__(meta, classname, bases, class_dict):
        cls = type.__new__(meta, classname, bases, class_dict)
        fields = []
        for k, v in class_dict.items():
            if isinstance(v, BaseField):
                v.name = k
                fields.append(v)

        fields.sort(key=lambda f: f.order)
        cls.fields = fields
        return cls


class Protocol(object):
    # field 1
    # field 2
    # ...

    __metaclass__ = ProtocolMeta

