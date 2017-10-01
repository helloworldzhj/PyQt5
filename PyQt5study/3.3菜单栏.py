# -*- coding: utf-8 -*-
"""菜单栏的使用"""
import sys
from PyQt5 import QtWidgets,QtGui

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		
		self.resize(250,150)
		self.setWindowTitle("菜单栏实例")
		
		exit_menu = QtWidgets.QAction(QtGui.QIcon(r"1.ico"),"退出",self)
		exit_menu.setShortcut("Ctrl+Q")
		exit_menu.setStatusTip("退出程序")
		exit_menu.triggered.connect(QtWidgets.qApp.quit)
		
		self.statusBar()
		
		menubar = self.menuBar()
		file = menubar.addMenu("文件")
		file.addAction(exit_menu)
		
app = QtWidgets.QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
sys.exit(app.exec_())
		
		
		
