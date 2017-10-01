# -*- coding: utf-8 -*-
"""显示悬停信息"""
import sys
from PyQt5 import QtWidgets, QtCore, QtGui


class Tooltip(QtWidgets.QWidget):
	def __init__(self,parent=None):
		QtWidgets.QWidget.__init__(self,parent)
		
		self.setGeometry(835,465,250,150)
		self.setWindowTitle("提示信息")
		
		self.setToolTip("This is a <b>QWidget<b> widget")
		# QtWidgets.QToolTip.setFont(QtGui.QFont("Times", 10))


app = QtWidgets.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())





