#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
This module provides many methods to interact with Strings and convert them into a specific format.
"""
def strToBool(s):
    """
    Convert an String representing a boolean into a boolean
    :param s: a boolean as a String
    :return: boolean
    """
    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        raise ValueError("Cannot covert {} to a bool".format(s))

def strUnderline(s):
    """
    Return an underline string of the same size of the String received in parameter.
    :param s: String
    :return: String
    """
    underline = ""
    for i in range(0, len(s)):
        underline += "="
    print(s)
    print(underline)