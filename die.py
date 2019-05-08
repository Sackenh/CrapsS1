#! /usr/bin/env python3
__author__ = 'Garrett Sacken'
from random import randint

class Die(object):


    def __init__(self, beginningSides = 6, beginningStartingValue = 1, beginningColor= "Bone"):
        self.numberOfSides = beginningSides
        self.startingValue = beginningStartingValue
        self.color = beginningColor
        self.value = self.numberOfSides

    def __str__(self):
        return "{0}".format(self.getValue())

    def getValue(self):
        return self.value

    def setValue(self, newValue = 0):
        self.value = newValue

    def getSides(self):
        return self.numberOfSides

    def roll(self):
        self.value = randint(self.startingValue, self.numberOfSides)
        return self.value
