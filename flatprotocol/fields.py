# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

from field_opts import *

__all__ = ['IntegerField', 'BinaryField',]


class BaseField(object):
    FIELD_ID = 0
    OPTS = FieldOptions

    def __init__(self, **kwargs):
        self.options = self.OPTS.make_opts(**kwargs)


class IntegerField(BaseField):
    FIELD_ID = 10
    OPTS = IntegerFieldOptions

class BinaryField(BaseField):
    FIELD_ID = 20
    OPTS = BinaryFieldOptions

