#!/usr/bin/python3
""" A script markdown2html.py that takes an argument 2 strings """
import sys
import os.path


if len(sys.argv) < 2:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

if not os.path.isfile(sys.argv[1]):
    print("Missing {}".format(sys.argv[1]), file=sys.stderr)
    exit(1)

exit(0)
