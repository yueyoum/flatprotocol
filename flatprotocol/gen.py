# -*- coding: utf-8 -*-
"""
Author:        Wang Chao <yueyoum@gmail.com>
Filename:      gen.py
Date created:  2014-11-28 13:30:18
Description:

"""

import os
import sys
import shutil
import optparse

from flatprotocol import templates


class Context(object):
    def __init__(self):
        self.language = None            # language to generate
        self.template = None            # language template engine
        self.modules = []               # protocol files imported as modules
        self.destination = None         # output directory

        self.parse_options()


    def parse_options(self):
        parse = optparse.OptionParser()
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

        try:
            t = getattr(templates, language)
        except AttributeError:
            parse.error("Language {0} Not Supported".format(language))
            return

        self.language = language
        self.template = t

        if not destination:
            destination_given = False
            destination = "flatprotocol_out_{0}".format(language)
        else:
            destination_given = True


        destination = os.path.abspath(destination)
        if os.path.exists(destination):
            if destination_given and os.listdir(destination):
                parse.error("Given directory Not Empty!")
            shutil.rmtree(destination)
        os.mkdir(destination)

        self.destination = destination

        for f in args:
            file_absdir = os.path.dirname(os.path.abspath(f))
            if file_absdir not in sys.path:
                sys.path.append(file_absdir)

            filename, ext = os.path.splitext(os.path.basename(f))
            if ext != '.py':
                print "Warning: {0} is Not a Python File, Ignore!".format(f)
                continue

            m = __import__(filename)
            m.spec._original_filename = filename
            self.modules.append(m)


        return t, destination, args

