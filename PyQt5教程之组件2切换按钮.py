#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QColor

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.col = QColor(0,0,0)
        #这里是初始化，让rgb值为黑色。
        
        redb = QPushButton('Red',self)
        redb.setCheckable(True)
        redb.move(10,10)
        #要创建按钮，就要创建QPushButton，并且调用setCheckable方法让它可被选中。
        redb.clicked[bool].connect(self.setColor)
        #我们把clicked信号连接到我们定义的方法上。我们使用clicked信号来操作布尔值。
        
        
        redb = QPushButton('Green',self)
        redb.setCheckable(True)
        redb.move(10,60)
        redb.clicked[bool].connect(self.setColor)
        
        blueb = QPushButton('Blue',self)
        blueb.setCheckable(True)
        blueb.move(10,110)
        blueb.clicked[bool].connect(self.setColor)
        
        self.square = QFrame(self)
        self.square.setGeometry(150,20,100,100)
        self.square.setStyleSheet('QWidget { background-color: %s }'%self.col.name())
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()
        
    def setColor(self,pressed):
        source = self.sender()
        #我们获得发生状态切换的按钮
        if pressed:
            val = 255
        else:
            val = 0
        if source.text() == 'Red':
            self.col.setRed(val)
            #在这种情况下如果发生切换的按钮red按钮，我们更新rgb中红色部分的值
        elif source.text() == 'Green':
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
            
        self.square.setStyleSheet("QFrame { background-color: %s }" %self.col.name())
        #我们使用样式表来改变背景颜色。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
        
#在这个例子中我们创建了三个切换按钮和一个QWidget组件。我们把QWidget组件的背景颜色设置成黑色。切换按钮将在红色绿色蓝色的rgb只部分切换。QWidget组件的背景颜色将取决于哪一个切换按钮被按下。
        
        