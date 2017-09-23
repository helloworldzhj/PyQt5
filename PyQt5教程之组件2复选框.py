#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        cb = QCheckBox('show title',self)
        #创建一个复选框，设置他的内容是showtitle 
        cb.move(20,20)
        cb.toggle()
        #我们需要设置窗口标题，所以我们必须选中复选框。如果不选中，默认情况下复选框不会被选中所以窗口标题也不会被设置
        cb.stateChanged.connect(self.changeTitle)
        #将我们定义的changetitle()槽方法和statechanged信号连接。changetitle方法用于切换窗口标题。
        
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('QCheckBox')
        self.show()
        
    def changeTitle(self,state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    #复选框组件的状态会传入changetitle方法的state参数。如果复选框被选中，我们设置窗口标题。否则我们把窗口标题设置成一个空字符串。
            
if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    
#在这个例子中我们使用复选框来切换标题