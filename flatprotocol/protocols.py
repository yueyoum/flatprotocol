# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from flatprotocol.fields import BaseField
from flatprotocol.utils import Singleton


__all__ = ['Protocol',]



class ProtocolMap(object):
    __metaclass__ = Singleton

    def __init__(self):
        self.name_id_maps = {}

    @property
    def id_name_maps(self):
        return {v: k for k, v in self.name_id_maps.iteritems()}

    def add(self, name, pid):
        self.name_id_maps[name] = pid



class ProtocolOptions(object):
    def __init__(self, cls, bases, attrs):
        self.protocol = cls
        self.name = cls.__name__
        self.bases = bases
        self.attrs = attrs
        self.fields = self.get_fields()


    def get_fields(self):
        fields = []
        for k, v in self.attrs.items():
            if isinstance(v, BaseField):
                v.name = k
                fields.append(v)

        fields.sort(key=lambda f: f.order)
        return fields

    def set_protocol_id(self, pid):
        self.protocol_id = pid
        ProtocolMap().add(self.name, pid)




class ProtocolBase(type):
    def __new__(cls, name, bases, attrs):
        cls = super(ProtocolBase, cls).__new__(cls, name, bases, attrs)
        cls._meta = ProtocolOptions(cls, bases, attrs)
        return cls


class Protocol(object):
    """
    The Base Protocol, All Protocols inherit from this.
    Protocol Information call find in cls._meta:

    cls._meta.protocol_id:  protocol id
    cls._meta.name:         protocol name
    cls._meta.fields:       protocol fields (Same order as the defination)
    """
    # fields defination
    # field 1
    # field 2
    # ...

    __metaclass__ = ProtocolBase

