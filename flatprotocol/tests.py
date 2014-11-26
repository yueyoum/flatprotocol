# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

import unittest

class TestProtocolFields(unittest.TestCase):
    def setUp(self):
        class P(Protocol):
            id = IntegerField()
            name = StringField()
            des = StringField(optional=True)
            bag = ListField()

        self.defined_protocol = P()

    def test_fields(self):
        fields = self.defined_protocol.get_fields()
        self.assertEqual(len(fields), 4)
        for f in fields:
            self.assertIn(f.name, ['id', 'name', 'des', 'bag'])
            if f.name == 'des':
                self.assertTrue(f.optional)



if __name__ == '__main__':
    import os
    import sys

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(project_path)

    from flatprotocol import *

    unittest.main()


