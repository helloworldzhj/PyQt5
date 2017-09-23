#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

os.chdir('C:/Users/Administrator/AppData/Local/Programs/Python/Python35-32/0/PyQt5教程_博客园')

class Example(QWidget):
     
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("redrock.png")
        #创建QPixmap对象。该对象构造方法传入一个文件的名字作为参数。
 
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        #把像素图对象设置给标签，从而通过标签来显示像素图。
 
        hbox.addWidget(lbl)
        self.setLayout(hbox)
        
        self.move(300, 200)
        self.setWindowTitle('Red Rock')
        self.show()
        #运行这个例子，我们会把一个图片显示在窗口上。

if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #运行这个例子，我们会把一个图片显示在窗口上。












