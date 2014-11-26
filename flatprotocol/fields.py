# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


__all__ = ['BaseField', 'IntegerField', 'FloatField', 'BinaryField', 'StringField',
           'Vector2Field', 'Vector3Field', 'ListField']


class BaseField(object):
    ORDER = 0
    FIELD_ID = 0

    def __init__(self, optional=False):
        self.optional = optional
        self.order = BaseField.ORDER
        BaseField.ORDER += 1


class IntegerField(BaseField):
    FIELD_ID = 10

class FloatField(BaseField):
    FIELD_ID = 20

class BinaryField(BaseField):
    FIELD_ID = 30

class StringField(BaseField):
    FIELD_ID = 40

class Vector2Field(BaseField):
    FIELD_ID = 50

class Vector3Field(BaseField):
    FIELD_ID = 60


class ListField(BaseField):
    FIELD_ID = 100
