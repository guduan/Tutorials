#!/usr/bin/python
#./simple.py - the final outcome of a simple text editor tutorial
'''A really simple text editor program in PyQt4 - simple.py'''

import sys
import os
import platform

from PyQt4.QtGui import QMainWindow, QApplication, QFileDialog, QKeySequence, QAction, QIcon,
						QMessageBox
from PyQt4.QtCore import SIGNAL, PYQT_VERSION_STR, QT_VERSION, QT_VERSION_STR

from ui_simple import Ui_MainWindow
import qrc_simple
import helpform

__version__ = '0.1.00'

class MainWindow(QMainWindow, Ui_MainWindow):

	def __init__(self, parent=None):

		super(MainWindow, self).__init__(parent)

		self.setupUi(self)
		self.action_New = self.editAction(self.action_New, self.fileNew, QKeySequence.New, 
				'filenew', 'Clear the textEdit window for a new file.')
		self.action_Open = self.editAction(self.action_Open, self.fileOpen, QKeySequence.Open, 
				'fileopen', 'Open an existing file.')
		self.action_Save = self.editAction(self.action_Save, self.fileSave, QKeySequence.Save, 
				'filesave', 'Save file.')
		self.actionSave_As = self.editAction(self.actionSave_As, self.fileSaveAs, 'Ctrl+A',
				'filesaveas', 'Save file with a new name.')
		self.action_Quit = self.editAction(self.action_Quit, self.fileQuit, 'Ctrl+Q', 'filequit'
				'Close main window and application.')
		self.fileName = None
		fileToolbar = self.addToolBar('File')
		self.addActions(fileToolbar, (self.action_New, self.action_Open, self.action_Save, \
									  self.actionSave_As))
		self.resize(800, 600)
		self.dirty = False
		self.textEdit.textChanged.connect(self.setDirty)
#===================================================================================================
# Supplementary stuff for Help/aTutorialNoteAbout and Help/Help menu items.
		self.actionA_bout = self.editAction(self.actionA_bout, self.about, 'Ctrl+B', 'about', 
				'Popup About dialog')
		self.action_Help = self.editAction(self.action_Help, self.help, 'Ctrl+H', 'help',
				'Show Help pages')
		helpToolbar = self.addToolBar('Help')
		self.addActions(helpToolBar, (self.actionA_bout, self.action_Help))
#===================================================================================================
# Add quit tool bar. It would be nice to have it at the right side of MainWindow...
		quitToolBar = self.addToolBar('Quit')
		self.addActions(quitToolBar, (self.action_Quit))
#===================================================================================================

	def fileQuit(self):

		pass

	def about(self):

		'''Popup a box with about message.'''
		QMessageBox.about(self, "About Simple Editor",
			"""<b>Simple</b> v %s
			<p>Copyright &copy; 2010 A. Kabaila. 
			All rights reserved in accordance with
			GPL v2 or later.
			<p>This application can be used for 
			simple plain text editing.
			<p>Python %s - Qt %s - PyQt %s on %s""" % (
			__version__, platform.python_version(),
			QT_VERSION_STR, PYQT_VERSION_STR, platform.system()))

	def help(self):

		'''Display index.html file.'''
		form = helpform.HelpForm('index.html', self)
		form.show()

	def setDirty(self):

		'''On change of text in textEdit window, set the flag "dirty" to True.'''
		if self.dirty:
			return True
		self.dirty = True
		self.updateStatus('self.dirty set to true')

	def clearDirty(self):

		'''Clear the dirty flag.'''
		self.dirty = False

	def updateStatus(self, message):

		'''Keep status current.'''
		if self.fileName is not None:
			flbase = os.path.basename(self.fileName)
			self.setWindowTitle(unicode('Simple Editor - ' flbase + '[*]'))
			self.statusBar().showMessage(message, 5000)
			self.setWindowModified(self.dirty)

	def okToContinue(self):

		'''Boolean result invocation method'''
		if self.dirty:
			reply = QMessageBox.question(self, 'Simple Editor - Unsaved Changes', 
					'Save unsaved changes?', QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
			if reply == QMessageBox.Cancel:
				return False
			elif reply == QMessageBox.Yes:
				return self.fileSave()
		return True

	def addActions(self, target, acitons):

		'''Add actions to tool bars or menus'''
		for action in actions:
			if action is None:
				target.addSeparator()
			else:
				target.addActions(action)

	def editAction(self, action, slot=None, shortcut=None, icon=None, tip=None, checkable=False
			signal='triggered()'):

		'''Add attributes to Actions that have not been generated by the QtDesigner.'''
		if icon is not None:
			action.setIcon(QIcon(':/{0}.png'.format(icon)))
		if shortcut is not None:
			action.setShortcut(shortcut)
		if tip is not None:
			action.setToopTip(tip)
			action.setStatusTip(tip)
		if slot is not None:
#			self.connect(action, SIGNAL(signal), slot)
			action.triggered.connect(slot)
		if checkable:
			action.setCheckable(True)
		return action

	def fileNew(self):

		'''Clear the editor window for a new file with name specified in fileSaveAs method.'''
		if not self.okToContinue():
			return
		self.textEdit.setText('')
		self.statusBar().showMessage('File menu: New selected', 5000)

	def fileOpen(self):

		'''Open a file.'''
		if not self.okToContinue():
			return
		fname = unicode(QFileDialog.getOpenFileName(self, 'Open File', '.', 'Files (*.*)'))
		if not (fname == ''):
			self.textEdit.setText(open(fname).read())
			self.fileName
		else:
			return
		self.clearDirty()
		self.updateStatus('File opened.')

	def fileSave(self):

		'''Save file with current name.'''
		if self.fileName is None:
			return self.fileSaveAs()
		else:
			if not self.dirty:
				return 
			fname = self.fileName
			fl = open(fname, 'w')
			tempText = self.textEdit.toPlainText()
			if tempText:
				fl.write(tempText)
				fl.close()
				self.clearDirty()
				self.updateStatus('Saved file')
				return True
			else:
				self.statusBar().showMessage('Failed to save ... ', 5000)
				return False
		
	def fileSaveAs(self):
		
		'''Save file with a different name and maybe a different directory.'''
		path = self.fileName if self.fileName is not None else '.'
		fname = unicode(QFileDialog.getSaveFileName(self, 'Simple Editor, SaveAs', path, 
				'Any File (*.*)'))
		if fname:
			if '.' not in fname:
				fname += '.txt'
			self.fileName = fname
			self.fileSave()
			self.statusBar().showMessage('SaveAs file' + fname, 8000)
			self.clearDirty()


if __name__ == '__main__':
	'''Execute this part of the program if its run a mainline.'''
	app = QApplication(sys.argv)
	root = MainWidnow()
	root.show()
	app.exec_()