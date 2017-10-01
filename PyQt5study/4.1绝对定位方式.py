# -*- coding: utf-8 -*-
"""绝对定位演示"""

import sys
from PyQt5 import QtWidgets,QtGui
	
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		
		self.setWindowTitle("绝对定位演示程序")
		self.resize(250,150)
		QtWidgets.QLabel('Couldn\'t',self).move(15,10)
		QtWidgets.QLabel('care',self).move(35,40)
		QtWidgets.QLabel('less',self).move(55,60)
		QtWidgets.QLabel('and',self).move(115,60)
		QtWidgets.QLabel('then',self).move(135,40)
		QtWidgets.QLabel('me',self).move(115,20)
		QtWidgets.QLabel('help',self).move(145,10)
		QtWidgets.QLabel('nothing',self).move(215,10)
		
app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec_())		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		




