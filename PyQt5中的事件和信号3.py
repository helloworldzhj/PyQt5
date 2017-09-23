#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
#事件发送者
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication

class Example(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		
	def initUI(self):
		btn1=QPushButton('Button 1',self)
		btn1.move(30,50)
		
		btn2=QPushButton('Button 2',self)
		btn2.move(150,50)
		
		btn1.clicked.connect(self.buttonClicked)
		btn2.clicked.connect(self.buttonClicked)
		#在这个例子中，我们有两个按钮，在click()方法中，我们调用sender()方法来判断哪一个按钮是我们按下的.
		#两个按钮连接到同一个槽中。
		
		self.statusBar()
		
		
		self.setGeometry(300,300,290,150)
		self.setWindowTitle('event sender')
		self.show()
		
	def buttonClicked(self):
		sender = self.sender()
		self.statusBar().showMessage(sender.text()+' was pressed')
		#我们调用sender方法判断发送信号的信号源是哪一个。然后在应用的状态栏上显示被按下的按钮的标签内容。
		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
		