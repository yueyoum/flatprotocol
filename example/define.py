# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from flatprotocol import *

spec = Specification()

@spec(protocol_id=1)
class Weapon(Protocol):
    xx = IntegerField()
    mm = StringField()
    aa = Vector2Field()


@spec(protocol_id=2)
class Person(Protocol):
    id = IntegerField()
    name = StringField(optional=True)
    aa = BinaryField()
    mm = ListField(IntegerField())

    # abcd = ListField(Weapon())


