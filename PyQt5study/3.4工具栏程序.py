# -*- coding: utf-8 -*-
"""工具栏的使用"""
import sys
from PyQt5 import QtWidgets,QtGui

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		
		self.resize(250,150)
		self.setWindowTitle("工具栏实例")
		
		self.exit_menu = QtWidgets.QAction(QtGui.QIcon(r"2.jpg"),"退出",self)
		self.exit_menu.setStatusTip("退出程序")
		self.exit_menu.setShortcut("Ctrl+Q")
		self.exit_menu.triggered.connect(QtWidgets.qApp.quit)
		
		self.toolbar = self.addToolBar("退出")
		self.toolbar.addAction(self.exit_menu)
		
app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())