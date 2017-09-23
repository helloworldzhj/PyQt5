#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        cal = QCalendarWidget(self)
        #创建QCalendarWidget类。
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)
        #如果我们在组件上选择了一个日期，clicked[QDate] 信号会被发射。我们把这个信号和自定义的showDate()方法连接。
         
        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)
         
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
    def showDate(self, date):
        self.lbl.setText(date.toString())
    #我们通过selectedDate()方法检索被选中的日期。然后我们把选中的日期对象转化成字符串显示在标签组件上。
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #这个例子展示了一个日历组件和标签组件。功能是日历中选择的日期会显示在标签组件中。