# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'


from flatprotocol.templates.base import BaseTemplate


PROTOCOL = """
class {class_name}({base}):
    PROTOCOL_ID = {protocol_id}
    def __init__(self):
{fields}

    def Parse(self, data):
        pass

    def Serialize(self):
        pass
"""



class Template(BaseTemplate):
    FILE_EXTENSION = '.py'
    FILE_COMMENT_SYMBOL = '#'

    def make_one_protocol(self, p):

        fields = []
        for f in p._meta.fields:
            fields.append("        self.{0} = None".format(f.name))

        fields = '\n'.join(fields)
        return PROTOCOL.format(
                class_name=p._meta.name,
                base='object',
                fields=fields,
                protocol_id=p._meta.protocol_id

                )

