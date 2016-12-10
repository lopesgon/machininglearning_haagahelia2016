#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""
This Data Access Object (DAO) module is in charge of writing into a log.txt file the ON/OFF events of the software.
"""

def writingLine(str):
    """
    Writes into a log.txt file the String received in parameter.
    :param str: a String reprensenting an event of the software
    """
    print(str)
    file = open("log.txt", "a")
    file.write(str)
    file.close()