#!/usr/bin/env python

import sys
from PySide import QtGui, QtCore

class Example(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.move(300, 300)
        self.setWindowTitle("Size Policy")
        self.initUI()

    def initUI(self):
        btn1 = QtGui.QPushButton("Button", self)
        btn1.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        btn2 = QtGui.QPushButton("Button", self)
        btn3 = QtGui.QPushButton("Button", self)
        btn3.setSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)

        layout = QtGui.QHBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        layout.addWidget(btn3)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtGui.QApplication([])
    root = Example()
    root.show()
    sys.exit(app.exec_())