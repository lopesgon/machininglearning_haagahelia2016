#!/usr/local/bin/python
# -*- coding: utf-8 -*-

DATA_FILES = "files.csv"

class ObjectsDao(object): #new

    @staticmethod
    def readLstFiles():
        #TO DO
        None

    @staticmethod
    def _readLine(lineFile):
        file = lineFile.split("\n")
        return file