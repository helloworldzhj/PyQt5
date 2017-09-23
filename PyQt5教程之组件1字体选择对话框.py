#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
 
class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		vbox = QVBoxLayout()
		btn = QPushButton('Dialog', self)
		btn.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
		btn.move(20, 20)
		vbox.addWidget(btn)
		btn.clicked.connect(self.showDialog)
		self.lbl = QLabel('Knowledge only matters', self)
		self.lbl.move(130, 20)
		vbox.addWidget(self.lbl)
		self.setLayout(vbox)
		self.setGeometry(300, 300, 250, 180)
		self.setWindowTitle('Font dialog')
		self.show()
	def showDialog(self):
		font, ok = QFontDialog.getFont()
		#在这儿弹出一个字体对话框。getFont方法返回字体名字和布尔值，如果用户点击了ok，布尔值为true；否则为false。
		if ok:
			self.lbl.setFont(font)
		#如果点击了OK按钮，标签字体会改变。
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
	#在这个例子中，我们有一个按钮和一个标签。通过字体选择对话框，我们可以改变标签内容的字体