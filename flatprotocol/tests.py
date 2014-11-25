# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

import unittest

class TestFieldOptions(unittest.TestCase):

    def test_unsupported_options(self):
        self.assertRaises(
            exception.UnsupportedKWargs,
            field_opts.FieldOptions.make_opts,
            hello=1
        )


    def test_integer_default_options(self):
        self.assertDictEqual(
            {'default': 0, 'optional': False},
            field_opts.IntegerFieldOptions.make_opts()
        )

    def test_integer_custom_options(self):
        self.assertDictEqual(
            {'default': 10, 'optional': False},
            field_opts.IntegerFieldOptions.make_opts(default=10)
        )

        self.assertDictEqual(
            {'default': 10, 'optional': True},
            field_opts.IntegerFieldOptions.make_opts(default=10, optional=True)
        )





if __name__ == '__main__':
    import os
    import sys

    project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(project_path)

    from flatprotocol import exception
    from flatprotocol import field_opts

    unittest.main()


