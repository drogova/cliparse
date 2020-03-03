import argparse
from typing import NoReturn
from cliparse.commands import parse


def execute() -> NoReturn:
    """Parse cmdline arguments"""
    parser = argparse.ArgumentParser(prog='cliparse')
    parser.add_argument('--xpath', metavar='NAME', default='//*', help='xpath in html', dest='name')

    args = parser.parse_args()
    parse.execute(args.name)
