# -*- coding: utf-8 -*-

__author__ = 'Wang Chao'
__date__ = '14-11-25'

import os
import sys
import shutil
from optparse import OptionParser
import inspect

from flatprotocol import Protocol
from flatprotocol import templates


def build_options():
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

    return parse

def check_and_prepare():
    parse = build_options()

    options, args = parse.parse_args()
    language = options.language
    destination = options.destination

    if not language:
        parse.error("Language not given")

    if not destination:
        destination_given = False
        destination = "flatprotocol_out_{0}".format(language)
    else:
        destination_given = True

    try:
        t = getattr(templates, language)
    except AttributeError:
        parse.error("Language {0} Not Supported".format(language))
        return

    destination = os.path.abspath(destination)
    if os.path.exists(destination):
        if destination_given and os.listdir(destination):
            parse.error("Given directory Not Empty!")
        shutil.rmtree(destination)
    os.mkdir(destination)

    for f in args:
        file_absdir = os.path.dirname(os.path.abspath(f))
        if file_absdir not in sys.path:
            sys.path.append(file_absdir)

    return t, args, destination




def generate():
    template_obj, args, destination = check_and_prepare()

    for f in args:
        file_name, ext = os.path.splitext(os.path.basename(f))
        if ext != '.py':
            print "Warning: {0} is Not a Python File, Ignore!".format(f)
            continue
        generate_one(template_obj, file_name, destination)


def generate_one(t, file_name, destination):
    module = __import__(file_name)

    result_file_name = os.path.join(destination, '{0}{1}'.format(file_name, t.FILE_NAME_EXTENSION))
    result_file = open(result_file_name, 'a')

    for name in dir(module):
        if name.startswith('__'):
            continue
        cls = getattr(module, name)
        if inspect.isclass(cls) and issubclass(cls, Protocol) and cls is not Protocol:
            result = t.generate(cls)
            result_file.write(result)

    result_file.close()

