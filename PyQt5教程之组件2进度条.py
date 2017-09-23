#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import (QWidget, QProgressBar,
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
 
 
class Example(QWidget):
     
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):     

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        #这是滑块条类的构造方法。

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        #用定时器对象来激活进度条。
         
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        #每个QObject类和它的子类都有timerEvent()事件处理函数用于处理定时事件。为了对定时器事件作出反馈，我们重新实现了这个事件处理函数。

    def doAction(self):
    
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
    #为了开启定时器事件，我们调用了start()方法。这个方法有两个参数：定时时间和接收定时器事件的对象。
    #在doAction()方法中，我们开始和停止定时器。
             
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
#在例子中有一个横向进度条和一个按钮。按钮控制滑块条的开始和停止。