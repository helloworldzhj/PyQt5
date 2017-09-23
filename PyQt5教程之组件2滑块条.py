#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Example(QWidget):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        #创建了一个横向的滑块条。
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        #我们把valuechange信号连接到我们自定义的changevalue()方法上
         
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('mute.png'))
        #我们创建了一个标签组件，并设置了一个初始的无声图片
        self.label.setGeometry(160, 40, 80, 30)
         
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
         
         
    def changeValue(self, value):
 
        if value == 0:
            self.label.setPixmap(QPixmap('mute.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('min.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('med.png'))
        else:
            self.label.setPixmap(QPixmap('max.png'))
        #在这里我们实现了根据滑块条的值，我们设置不同的标签图片。在上面的代码中，如果滑块条的值等于0，我们为标签设置mute。png图片
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

#在这个例子中，我们创建了一个音量控制器。通过拖动滑块条的把手，我们可以改变标签的图像。





