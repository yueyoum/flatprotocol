# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from flatprotocol import *

class Person(Protocol):
    id = IntegerField()
    name = BinaryField(default="Jim", optional=True)

    class Meta:
        protocol_id = 1

