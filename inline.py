#!/usr/bin/env python3

import argparse
import sys
from os import path
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Inline JS and CSS into HTML")
parser.add_argument('-e', '--entry', help='HTML entry file')
parser.add_argument(
    '-o', '--output', help='HTML output file', default='out.html')
parser.add_argument('-j', '--javascript',
                    help="JavaScript source directory", default='.')
parser.add_argument('-c', '--css', help='CSS source directory', default='.')
args = parser.parse_args()

if args.entry:
    entryFp = open(args.entry)
else:
    entryFp = sys.stdin

# open the main html file
soup = BeautifulSoup(entryFp, 'html.parser')

# JavaScript
scripts = soup.find_all("script", inline=True)
for script in scripts:
    # replace each <script inline>
    with open(path.join(args.javascript, script['src'])) as src:
        del script['src']
        del script['inline']
        script.string = src.read()

# CSS
links = soup.find_all("link", rel="stylesheet", inline=True)
for link in links:
    with open(path.join(args.css, link["href"])) as sheet:
        style = soup.new_tag("style")
        style.string = sheet.read()
        link.replace_with(style)

with open(args.output, "w") as out:
    # write out the final html file, everything inlined
    out.write(str(soup))

entryFp.close()
