#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''绝对定位import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication

class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		
		lbl1 = QLabel('Zetcode', self)
		lbl1.move(15, 10)

		lbl2 = QLabel('tutorials', self)
		lbl2.move(35, 40)
		
		lbl3 = QLabel('for programmers', self)
		lbl3.move(55, 70)
		
		self.setGeometry(300, 300, 250, 150)
		self.setWindowTitle('Absolute')
		self.show()
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())'''
	
'''箱布局import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication)
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):
         
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
		#这里我们创建了两个按钮
 
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
		#这里我们创建了一个水平箱布局，并且增加了一个拉伸因子和两个按钮。拉伸因子自两个按钮之前增加了一个可伸缩空间。这会将按钮推到窗口的右边。
 
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
		#为了创建必要的布局，我们把水平布局放置在垂直布局内。拉伸因子将把包含两个按钮的水平箱布局推到窗口的底边
         
        self.setLayout(vbox)
		#最后设置一下窗口的主布局
         
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())'''
	

'''import sys网格布局
from PyQt5.QtWidgets import (QWidget,QGridLayout,QPushButton,QApplication)
class Example(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		grid = QGridLayout()
		self.setLayout(grid)
		#在这个例子中，创建了一个全是按钮的网格布局。实例化QGridLayout类，并且把这个类设为应用窗口的布局
		names = ['cls','bck','','close',
				'7','8','9','/',
				'4','5','6','*',
				'1','2','3','-',
				'0','.','=','+']
		#这些标签会在之后的按钮中使用
		positions = [(i,j) for i in range(5)for j in range(4)]
		#我们创建了一个网格的定位列表。
		for position , name in zip(positions,names):
			if name == '':
				continue
			button = QPushButton(name)
			grid.addWidget(button,*position)
		#创建出按钮，使用add Widget（）方法向布局中添加按钮。	
		self.move(300,150)
		self.setWindowTitle('Calculator')
		self.show()
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

#最常用的布局类是网格布局。这个布局使用行了列分割空间。要创建一个网格布局，我们需要使用QGridLayout类。'''


import sys文本审阅窗口示例
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
	QTextEdit, QGridLayout, QApplication)
	
	
class Example(QWidget):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		
		
	def initUI(self):
		title = QLabel('Title')
		author = QLabel('Author')
		review = QLabel('Review')
		
		titleEdit = QLineEdit()
		authorEdit = QLineEdit()
		reviewEdit = QTextEdit()

		grid = QGridLayout()
		grid.setSpacing(10)
 
		grid.addWidget(title, 1, 0)
		grid.addWidget(titleEdit, 1, 1)
 
		grid.addWidget(author, 2, 0)
		grid.addWidget(authorEdit, 2, 1)
 
		grid.addWidget(review, 3, 0)
		grid.addWidget(reviewEdit, 3, 1, 5, 1)
		
		self.setLayout(grid)
		
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Review')   
		self.show()
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
		
		
		
		
		
		
		
		
		
		
		
		
		
		