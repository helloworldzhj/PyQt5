#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import (QWidget, QLabel,
    QLineEdit, QApplication)
 
 
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        #创建单行文本编辑框（QLineEdit）组件。
        qle.move(60, 100)
        self.lbl.move(60, 40)
 
        qle.textChanged[str].connect(self.onChanged)
        #如果单行文本编辑框框内文本被改变，调用onChanged()方法。
         
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()
        #上面是onChanged()方法的实现，我们设置了标签的显示文本。我们调用了adjustSize()方法来调整标签相对于显示的文本的长度。
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
    #这个例子显示了一个单行编辑文本框和一个标签。我们在单行文本编辑框中输入文本时会同步把文本显示在标签中。