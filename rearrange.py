#!/usr/bin/env python3
"""
Function: rearrange_name
Params: name
Return: string
Description: Rearranging the given name by
swapping the first name with the last name
and vice versa. If there is only one word in
the string, return the string as is.
Author: Akanimoh George
"""
import re


def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])
