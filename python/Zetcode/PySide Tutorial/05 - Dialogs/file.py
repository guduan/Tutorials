#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
ZetCode PySide tutorial

In this example, we select a file with a QtGui.QFileDialog and display its
contents in a QtGui.QTextEdit.
Author: Jan Bodnar
Website: zetcode.com
Last Edited: August 2011
"""

import sys
from PySide import QtGui

class Example(QtGui.QMainWindow):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QtGui.QAction(QtGui.QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File Dialog')
        self.show()

    def showDialog(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open File', '/home')
        with open(fname, 'r') as f:
            data = f.read()
            self.textEdit.setText(data)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()