# -*- coding: utf-8 -*-
"""综合使用的程序"""
import sys
from PyQt5 import QtWidgets,QtGui

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()

		self.resize(250,150)
		self.setWindowTitle("我的程序")
		text_edit = QtWidgets.QTextEdit()
		self.setCentralWidget(text_edit)
		
		exit_action = QtWidgets.QAction(QtGui.QIcon(r"sample.png"),"退出",self)
		exit_action.setShortcut("Ctrl+Q")
		exit_action.setStatusTip("退出程序")
		exit_action.triggered.connect(QtWidgets.qApp.quit)
		
		self.statusBar()
		
		self.menu_bar = self.menuBar()
		file = self.menu_bar.addMenu("文件")
		file.addAction(exit_action)
		
		self.toolbar = self.addToolBar("退出")
		self.toolbar.addAction(exit_action)
		
app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())
		
		
		
		
		
		
		
		
		
		
		
		
		
		