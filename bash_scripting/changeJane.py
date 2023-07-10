#!/usr/bin/env python3
"""
Script to change the name of a file
"""
import sys
import subprocess

with open(sys.argv[1]) as my_file:
    data = my_file.readlines()
    for line in data:
        old_name = line.strip()
        new_name = old_name.replace("jane", "jdoe")
        subprocess.run(["mv", old_name, new_name])
    my_file.close()