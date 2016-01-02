#!/usr/bin/env python

from prettifier import prettify

if __name__ == '__main__':
    import sys
    import ast

    if len(sys.argv) != 2:
        print 'usage : python run_prettify.py <number> \nYou must specify the number to be prettified'
        sys.exit(1)

    try:
        #Usage of ast is the safe 'eval' for string to numbers
        print prettify(ast.literal_eval(sys.argv[1]))
    except Exception, e:
        raise ValueError('The type is not a numeric value') 