# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from fields import *


__all__ = ['Protocol',]


class Protocol(object):
    # field 1
    # field 2
    # ...

    @classmethod
    def get_fields(cls):
        fields = []
        for p in dir(cls):
            field = getattr(cls, p)
            if isinstance(field, BaseField):
                field.name = p
                fields.append(field)

        return fields

    def __init__(self):
        self.optional_fields = [f for f in self.get_fields() if f.optional]


    class Meta:
        protocol_id = None


