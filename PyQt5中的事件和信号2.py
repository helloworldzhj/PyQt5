#!/usr/bin/python3
# -*- coding: utf-8 -*-

#重写事件处理函数
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication

class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):     
			
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Event handler')
		self.show()
		
			
	def keyPressEvent(self, e):
	
		if e.key() == Qt.Key_Escape:
			self.close()
	#在这个例子中，我们重写了keypressevent事件处理函数
	#如果我们点了esc按钮，应用将会被终止
		
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())