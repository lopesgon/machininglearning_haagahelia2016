#!/usr/local/bin/python
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, nom, prenom, age):
        self._nom = nom
        self._prenom = prenom
        self._age = age

    @property
    def prenom(self):
        return self._prenom

    @property
    def nom(self):
        return self._nom

    @property
    def age(self):
        return self._age

    @prenom.setter
    def _set_prenom(self, p):
        print
        "Changement du prenom"
        self._prenom = p

    def __str__(self):
        return self.nom + " " + self.prenom + " " + str(self.age)

    def _repr_(self):
        return self.__str__()

    def _save_(self):
        return self.nom + ";" + self.prenom + ";" + str(self.age)
