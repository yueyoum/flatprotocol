# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-26'


__all__ = ['Specification',]


class Specification(object):
    def __init__(self, filename=None):
        self._filename = filename
        self._original_filename = None
        self.protocols = []

    def __call__(self, protocol_id):
        def wrap(cls):
            cls._meta.set_protocol_id(protocol_id)
            self.protocols.append(cls)
            return cls
        return wrap

    @property
    def filename(self):
        if self._filename:
            return self._filename
        return self._original_filename

