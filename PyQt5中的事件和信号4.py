#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
	closeApp = pyqtSignal()
	#信号使用了pyqtSignal方法创建并且成为外部类Communicate类的属性
	
class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):
		self.c = Communicate()
		self.c.closeApp.connect(self.close)
		#把自定义的closeApp信号连接到QMainWindow的close()槽上。
		
		self.setGeometry(300, 300, 290, 150)
		self.setWindowTitle('Emit signal')
		self.show()
	def mousePressEvent(self,event):
		self.c.closeApp.emit()
		#当我在窗口上点击一下鼠标，closeApp信号会被发射。应用中断。
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
	
#我们创建了一个新的信号叫做closeApp当触发鼠标点击事件时信号就会被发射。信号连接到了QMainWindow的close（）方法。