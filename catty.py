#!/usr/bin/env python3
"""Prints out the contents of a file"""

import sys

def catty():
    with open(sys.argv[1]) as file:
        print(file.read())

catty()
