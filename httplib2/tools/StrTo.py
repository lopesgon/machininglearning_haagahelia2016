#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class StrTo(object):

    @staticmethod
    def strToBool(s):
        if s == 'true':
            return True
        elif s == 'false':
            return False
        else:
            raise ValueError("Cannot covert {} to a bool".format(s))

    @staticmethod
    def strUnderline(s):
        underline = ""
        for i in range(0, len(s)):
            underline += "="
        print(s)
        print(underline)