# MIT License

# Copyright (c) 2019 Alexandre Yukio Harano

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
"""yav's package command line interface."""

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys

from .core import YAValidator, BaseYAVException



RAW_DESCRIPTION = (r"""
__   __   _
\ \ / /__| |_
 \ V / _ \ __|
  | |  __/ |_
  |_|\___|\__|


             _                _   _
            / \   _ __   ___ | |_| |__   ___ _ __
           / _ \ | '_ \ / _ \| __| '_ \ / _ \ '__|
          / ___ \| | | | (_) | |_| | | |  __/ |
         /_/   \_\_| |_|\___/ \__|_| |_|\___|_|


                __     __    _ _     _       _
                \ \   / /_ _| (_) __| | __ _| |_ ___  _ __
                 \ \ / / _` | | |/ _` |/ _` | __/ _ \| '__|
                  \ V / (_| | | | (_| | (_| | || (_) | |
                   \_/ \__,_|_|_|\__,_|\__,_|\__\___/|_|




Yet Another Validator is a command line interface to validate
if each given parameter is valid against the following rules:

 (i) an integer bigger than 100_000 and smaller than 999_999, and

 (ii) digits cannot be repeated aparted by one digit (e.g.: 12145; 12325).
""")



def cli(args=None):

    if args is None:
        args = sys.argv[1:]

    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=RAW_DESCRIPTION,
    )

    parser.add_argument(
        'to_be_validated',
        metavar='to_be_validated',
        nargs='+',
        help=(
            'One or more parameters to be validated against rules'
        ),
    )

    if not args:
        args = ['--help']

    argument_namespace = parser.parse_args(args)
    validator = YAValidator()

    for arg in argument_namespace.to_be_validated:
        try:
            validator(value=arg)
        except BaseYAVException as exception:
            print(
                "- {0} is not valid:\t{1}."
                .format(arg, exception)
            )
        else:
            print("* {0} is valid!".format(arg))
