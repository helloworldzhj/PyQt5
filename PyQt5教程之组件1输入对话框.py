#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
'''对话框窗口或对话框是大多数主流GUI应用不可缺少的部分。对话是两个或更多人之间的会话。在计算机应用中，对话框是一个用来和应用对话的窗口。对话框可以用来输入数据，修改数据，改变应用设置等等。'''

import sys
from PyQt5.QtWidgets import *

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		self.btn = QPushButton('dialog',self)
		self.btn.move(20,20)
		self.btn.clicked.connect(self.showDialog)
		#一个按钮，一个单行编辑框组件。按下按钮会显示输入对话框，用于获得一个字符串值
		
		self.le = QLineEdit(self)
		self.le.move(130,22)
		
		self.setGeometry(300,300,290,150)
		self.setWindowTitle('Input Dialog')
		self.show()
	def showDialog(self):
		text,ok = QInputDialog.getText(self,'Input Dialog','Enter your name:')
		#第一个字符串参数是对话框的标题，第二个字符串参数是对话框内的消息文本。对话框返回输入的文本内容和一个布尔值。如果我们点击了Ok按钮，布尔值就是true，反之布尔值是false（译者注：也只有按下Ok按钮时，返回的文本内容才会有值）。
		if ok:
			self.le.setText(str(text))
			#把我们从对话框接收到的文本设置到单行编辑框组件上显示。
			#在对话框中输入的值会在单行文本框中显示
			
if __name__=='__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
