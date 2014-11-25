# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

import os
import shutil
from optparse import OptionParser

from flatprotocol import Protocol
from flatprotocol import templates

def generate():
    parse = OptionParser()
    parse.add_option(
        "-l", "--language",
        dest="language",
        help="Language to generate",
    )
    parse.add_option(
        "-o",
        dest="destination",
        help="Destination directory to place the generated files"
    )

    options, args = parse.parse_args()
    language = options.language
    destination = options.destination

    if not language:
        parse.error("Language not given")

    if not destination:
        destination = "flatprotocol_out_{0}".format(language)

    try:
        t = getattr(templates, language)
    except AttributeError:
        parse.error("Language {0} Not Supported".format(language))
        return

    destination = os.path.abspath(destination)
    shutil.rmtree(destination)
    os.pardir.makedirs(destination)

    for f in args:
        file_name, file_extension_name = os.path.splitext(f)
        generate_one(t, file_name, destination)


def generate_one(t, file_name, destination):
    print t, file_name, destination
    module = __import__(file_name)
    for cls in dir(module):
        if isinstance(cls, Protocol):
            print t.generate(cls)

