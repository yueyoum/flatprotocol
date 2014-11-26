# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

import datetime

from flatprotocol import *


TEMPLATE = """
# -*- coding: utf-8 -*-
# Generated by Flatprotocol
# Generated Date: {date}

class {class_name}(object):
    PROTOCOL_ID = {protocol_id}

    def __init__(self):
{fields}

    def Parse(self, data):
        pass

    def Serialize(self):
        pass
"""

FILE_NAME_EXTENSION = ".py"


def get_default_value(field):
    if isinstance(field, IntegerField):
        return 0
    if isinstance(field, FloatField):
        return 0
    if isinstance(field, BinaryField):
        return '""'
    if isinstance(field, StringField):
        return '""'
    if isinstance(field, Vector2Field):
        return (0, 0)
    if isinstance(field, Vector3Field):
        return (0,0,0)
    if isinstance(field, ListField):
        return []

def generate(cls):
    """

    :type cls: flatprotocol.Protocol
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    class_name = cls.__name__
    protocol_id = cls.Meta.protocol_id

    fields = []
    for p in dir(cls):
        field = getattr(cls, p)
        if isinstance(field, BaseField):
            fields.append("        self.{0} = {1}".format(p, get_default_value(field)))

    fields = '\n'.join(fields)

    result = TEMPLATE.format(
        date=now,
        class_name=class_name,
        protocol_id=protocol_id,
        fields=fields
    )

    return result
