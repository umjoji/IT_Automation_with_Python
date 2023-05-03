#!/usr/bin/env python3

import os
import sys
import re

def error_search(log_file):
    """
    Takes a log file and returns the errors spcified in the input
    or all if none specified
    """
    error = input("What are the errors you want too search for?\
                   Seperate with a space. ")
    returned_errors = []

    with open(log_file, mode="r", encoding="UTF-8") as file:
        for log in file.readlines():
            # list to store patterns to search
            error_patterns = ["error"]
            for i in range(len(error.split(" "))):
                error_patterns.append(r"{}".format(error.split(" ")[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()

    return returned_errors

def file_output(returned_errors):
    """Writes all the errors given in the list parameter to a file"""
    with open("Enter file path of where you want the error log to be: ", "w") as file:
        for error in returned_errors:
            file.write(error)
        file.close()

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)



