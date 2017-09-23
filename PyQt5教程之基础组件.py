#!/usr/bin/env python
# -*- coding:utf-8-*-

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QFont 
from PyQt5.QtCore import QCoreApplication

os.chdir('C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/0/PyQt5教程_博客园')

class Example(QMainWindow):
#在面向对象编程中有三个重要的东西，分别是类，数据，和方法。这里我们创建了一个新类叫做Example，Example类继承自QWidget类。这意味着我们调用了两个构造方法：第一个是Example类的构造方法，第二个是被继承类的构造方法。super()方法返回了Example类的父类的构造方法。并且我们调用了父类的构造方法。__init__()方法是python语言中的构造方法

	
	def __init__(self):
		super().__init__()
		self.initUI()
		#Gui的创建授予initUI（）方法完成。
	
	def initUI(self):
		#QAction是一个用于菜单栏、工具栏或自定义快捷键的抽象动作行为。
		exitAction1 = QAction(QIcon('exit.png'), '&Exit', self)
		exitAction1.setShortcut('Ctrl+Q')
		#创建了一个有指定图标和文本为'Exit'的标签。另外，还为这个动作定义了一个快捷键。
		exitAction1.setStatusTip('Exit application')
		exitAction1.triggered.connect(qApp.quit)
		self.statusBar()
		
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(exitAction1)
		#我们创建了有一个菜单项的菜单栏。这个菜单项包含一个选中后中断应用的动作。
		exitAction2 = QAction(QIcon('exit24.png'), 'Exit', self)
		exitAction2.setShortcut('Ctrl+Q')
		exitAction2.setStatusTip('Exit application')
		exitAction2.triggered.connect(qApp.quit)
		#创建了一个动作对象，和之前菜单栏中的部分代码相似。这个动作有一个标签，图标和快捷键。并且将QtGui.QMainWindow的quit()方法连接到了触发信号上。
		self.toolbar = self.addToolBar('Exit')
		self.toolbar.addAction(exitAction2)
		#我们创建了一个简单的工具栏。工具栏有一个动作，当这个退出动作被触发时应用将会被中断。
		
		
		self.setWindowIcon(QIcon('123.png'))#三个方法都继承自QWidget类。setGeometry()做了两件事：将窗口在屏幕上显示，并设置了它的尺寸。setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。事实上，这是将resize()和move()方法融合在一个方法内。为了做好这个例子，我们创建了一个QIcon对象。QIcon对象接收一个我们要显示的图片路径作为参数。
		QToolTip.setFont(QFont('SansSerif', 10))
		#这个静态方法设置了用于提示框的字体。我们使用10px大小的SansSerif字体。
		self.setToolTip('This is a <b>QWidget</b> widget')
		#为了创建提示框，我们调用了setTooltip()方法。我们可以在提示框中使用富文本格式。
		btn = QPushButton('Button', self)
		btn.setToolTip('This is a <b>QPushButton</b> widget')
		#我们创建了一个按钮组件并且为它设置一个提示框。
		btn.resize(btn.sizeHint())
		btn.move(50, 70)
		#这里改变了按钮的大小，并移动了在窗口上的位置。setHint()方法给了按钮一个推荐的大小。
		qbtn = QPushButton('Quit', self)
		qbtn.clicked.connect(QCoreApplication.instance().quit)
		qbtn.resize(qbtn.sizeHint())
		qbtn.move(150, 70)
		
		self.statusBar().showMessage('Ready')
		#状态栏又QMainWindow组件帮助创建完成（依赖于QMainWindow组件）。
		#为了得到状态栏，我们调用了QtGui.QMainWindow类的statusBar()方法。第一次调用这个方法创建了一个状态栏。随后方法返回状态栏对象。然后用showMessage()方法在状态栏上显示一些信息。
		
		self.setGeometry(300,300,500,500)
		#self.resize(400,400)
		#self.center()
		#将窗口居中
		self.setWindowTitle('朱华建')
		self.show()
		
	def center(self):
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
		
	def closeEvent(self, event):
		
		reply = QMessageBox.question(self, 'Message',
			"Are you sure to quit?", QMessageBox.Yes |
			QMessageBox.No, QMessageBox.No)

		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
	#应用和example对象被创建。主循环被启动。
	
#这段主要是给图形化界面添加了一些必要的组件，比如说按钮，工具栏，状态栏之类的。
