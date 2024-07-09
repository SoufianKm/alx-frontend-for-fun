#!/usr/bin/python3
""" A script markdown2html.py that takes an argument 2 strings """
import sys
import os.path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    else:
        with open(sys.argv[1], "r") as r:
            with open(sys.argv[2], "w") as w:
                for line in r:
                    length = len(line)
                    heading_content = line.lstrip('#')
                    heading_nbr = length - len(heading_content)
                    # headings
                    if heading_nbr in range(1, 6):
                        html_line = '<h{}>'.format(
                                heading_nbr) + heading_content.strip() +
                        '</h{}>\n'.format(heading_nbr)
                        w.write(html_line)
        exit(0)
