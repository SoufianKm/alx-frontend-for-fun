#!/usr/bin/python3
""" A script markdown2html.py that takes an argument 2 strings """
import sys
import os.path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)

    """Check if markdown file exist"""
    if not os.path.isfile(sys.argv[1]):
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
    else:
        with open(sys.argv[1], "r") as r:
            with open(sys.argv[2], "w") as w:
                start_ul = False
                for line in r:
                    length = len(line)
                    heading_content = line.lstrip('#')
                    heading_nbr = length - len(heading_content)
                    unordered_content = line.lstrip('-')
                    unordered_nbr = length - len(unordered_content)
                    # headings
                    if heading_nbr in range(1, 6):
                        html_line = '<h{}>{}</h{}>\n'.format(
                                heading_nbr, heading_content.strip(), heading_nbr)
                        w.write(html_line)
                    
                    # Unordered Listing
                    if unordered_nbr:
                        if not start_ul:
                            w.write('<ul>\n')
                            start_ul = True
                        html_line = '<li>{}<li>\n'.format(unordered_content.strip())
                        w.write(html_line)
                    if start_ul and  not unordered_nbr:
                        w.write('</ul>\n')
                        start_ul = False
                if start_ul:
                    w.write('</ul>\n')

        exit(0)
