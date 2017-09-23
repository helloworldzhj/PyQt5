#!/usr/bin/python3
# -*- coding: utf-8 -*-

#信号 & 槽
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,QVBoxLayout, QApplication)
#在这个例子中，我们显示了一个QtGui。QLCDNumber和一个QtGui.QSlider类，我们拖动滑块条的把手，lcd数字会变。

class Example(QWidget):
	def __init__(self):
		super().__init__()
		
		self.initUI()
	def initUI(self):
		lcd = QLCDNumber(self)
		sld = QSlider(Qt.Horizontal,self)
		
		vbox = QVBoxLayout()
		vbox.addWidget(lcd)
		vbox.addWidget(sld)
		
		self.setLayout(vbox)
		sld.valueChanged.connect(lcd.display)
		#这里我们将滑块条的valuechange信号与ld数字显示的display槽连接在一起
		#发送者是一个发送了信号的对象，接受者是一个接受了信号的对象。槽是对信号做出反应的方法
		self.setGeometry(300,300,250,150)
		self.setWindowTitle('Signal & slot')
		self.show()
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())