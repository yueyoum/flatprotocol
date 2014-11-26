# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-26'


__all__ = ['Specification',]


class Specification(object):
    def __init__(self, output_file_name=None):
        self.output_file_name = output_file_name
        self.protocols = []

    def __call__(self, protocol_id):
        print "==== call ", protocol_id
        def wrap(cls):
            cls.protocol_id = protocol_id
            self.protocols.append(cls)
            return cls
        return wrap

