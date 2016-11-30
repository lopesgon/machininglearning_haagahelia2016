#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#Software Engineering Project
#Machining Learning - Gathering behaviour in an indoor environment
#Frédéric Lopes Gonçalves Magalhaes (a1602054) & Nicolas Delbiaggio (a1602052)
#2016-2017, semester 5

from softwareproject.gatherbehavior.GatherControler import *
from softwareproject.base.TestingDao import writingLine
import os
import datetime

if __name__ == "__main__":
    writingLine("Software Engineering Project - SOFTWARE TURNING ON TIME : " + str(datetime.datetime.today()) + "\n\n")
    run()
    writingLine("SOFTWARE TURNING OFF TIME: " + str(datetime.datetime.today()) + "\n\n")
    os._exit(0)