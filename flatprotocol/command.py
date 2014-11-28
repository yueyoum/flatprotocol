# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

from flatprotocol.protocols import ProtocolMap
from flatprotocol.gen import Context


def generate():
    context = Context()
    print context.language
    print context.template
    print context.modules
    print context.destination

    print ProtocolMap().name_id_maps

    for m in context.modules:
        template = context.template.Template(context.destination, m)
        template.make()

