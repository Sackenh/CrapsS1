#! /usr/bin/env python3
__author__ = 'Garrett Sacken'
from die import *
import sys
import diceResources_rc
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import(QMainWindow, QWidget, QApplication)


class Dice(QMainWindow):
    die1 = die2 = None

    def __init__(self, parent=None):
        """Build a game with two di;;ce."""
        super().__init__(parent)
        uic.loadUi("Dice.ui", self)
        self.die1 = Die()
        self.die2 = Die()
        self.rollButton.clicked.connect(self.rollButtonClickedHandler)

    def __str__(self):
        """String representation for Dice."""
        return "Die1: %s\nDie2: %s" % ( self.die1, self.die2)

    def updateUI(self):
        self.die1View.setPixmap(QtGui.QPixmap(":/" + str(self.die1.getValue())))
        self.die2View.setPixmap(QtGui.QPixmap(":/" + str(self.die2.getValue())))
        pass

#@QtCore.pyqtSignature("")# Player asked for another roll of the dice.
    def rollButtonClickedHandler ( self ):
        print("Roll button clicked")
        self.die1.roll()
        self.die2.roll()
        self.updateUI()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    diceApp = Dice()
    diceApp.updateUI()
    diceApp.show()
    sys.exit(app.exec_())