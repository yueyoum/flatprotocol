# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

import unittest

class TestFieldOptions(unittest.TestCase):

    def test_unsupported_options(self):
        self.assertRaises(
            flatprotocol.exception.UnsupportedFieldOptions,
            flatprotocol.field_opts.BaseFieldOptions.make_opts,
            type('a', (object,), {}),
            hello=1
        )

    def test_optional(self):
        filed = IntegerField()
        self.assertEqual(
            filed.optional,
            False
        )

        filed = IntegerField(optional=True)
        self.assertEqual(
            filed.optional,
            True
        )


if __name__ == '__main__':
    import os
    import sys

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(project_path)


    import flatprotocol.exception
    import flatprotocol.field_opts
    from flatprotocol import *

    unittest.main()


