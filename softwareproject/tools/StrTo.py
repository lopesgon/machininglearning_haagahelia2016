#!/usr/local/bin/python
# -*- coding: utf-8 -*-

def strToBool(s):
    if s == 'true':
        return True
    elif s == 'false':
        return False
    else:
        raise ValueError("Cannot covert {} to a bool".format(s))

def strUnderline(s):
    underline = ""
    for i in range(0, len(s)):
        underline += "="
    print(s)
    print(underline)