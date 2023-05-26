from svgelements import *
import io
import os
import argparse

from parser.parser import Parser


def parse(filename):
    q = io.FileIO(filename)
    svg = SVG.parse(q)

    parser = Parser()
    nodes = parser.extract_nodes(svg)
    print(nodes)

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='svg-dot-parser',
                    description='Parse svg file to dot',
                    epilog='')
    parser.add_argument('filename')
    args = parser.parse_args()



    parse(args.filename)