# -*- coding: utf-8 -*-
"""窗口放在屏幕中间"""
import sys
from PyQt5 import QtWidgets

class Center(QtWidgets.QWidget):
	def __init__(self,parent=None):
		QtWidgets.QWidget.__init__(self,parent)
		self.setWindowTitle("窗口置中程序")
		self.resize(250,150)
		self.center()
		
	def center(self):
		screen = QtWidgets.QDesktopWidget().screenGeometry()
		size = self.geometry()
		self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

app = QtWidgets.QApplication(sys.argv)
center = Center()
center.show()
sys.exit(app.exec_())
























