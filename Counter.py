'''
Author: sunke 375352086@qq.com
Date: 2024-11-21 18:57:00
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-21 20:03:22
FilePath: /PyQT_Practice/Counter.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
使用线程类(QThread)编写计数器

基本原理
QThread派生一个子类
在这个子类里面定义一个run方法
def run(self):
    while True:
    # 每循环一次，休眠一秒钟
        self.sleep(1)
        # 当前循环等于5，直接退出
        if sec == 5:
            break;

QLCDNumber控件


WorkThread(QThread)
用到自定义信号
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


# 定义一个变量
sec = 0
num = 5
class WorkThread(QThread):
    timer = pyqtSignal()   # 每隔1秒发送一次信号
    end = pyqtSignal()     # 计数完成后发送一次信号
    def run(self):
        while True:
            self.sleep(1)  # 休眠1秒
            if sec == num:
                self.end.emit() # 发送end信号
                print('end')
                break
            print(num)
            self.timer.emit()  # 发送timer信号


class Counter(QWidget):
    def __init__(self,parent=None):
        super(Counter, self).__init__(parent)

        self.setWindowTitle("使用线程类(QThread)编写计数器")
        self.resize(300,200)

        # 创建垂直布局
        layout = QVBoxLayout()
        self.lcdNumber = QLCDNumber()
        layout.addWidget(self.lcdNumber)

        button = QPushButton('开始计数')
        self.lineEdit = QLineEdit('设置计数值')
        layout.addWidget(self.lineEdit)
        layout.addWidget(button)


        # 创建工作线程对象
        self.workThread = WorkThread()

        # 绑定 信号 槽


        self.workThread.timer.connect(self.countTime)
        self.workThread.end.connect(self.end)
        # 槽和按钮的单击事件
        button.clicked.connect(self.work)

        

        # 应用于垂直布局
        self.setLayout(layout)

    # 槽方法
    def countTime(self):
        # global 声明全局变量
        global sec
        sec += 1
        self.lcdNumber.display(sec)

    def end(self):
        global sec
        QMessageBox.information(self,'消息','计数结束',QMessageBox.Ok)
        sec = 0

    def work(self):
        global num
        num = int(self.lineEdit.text())
        if(num):
         self.workThread.start()
        else:
            QMessageBox.information(self,'告警','输入计数值',QMessageBox.Ok)
        print(num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo =Counter()
    demo.show()
    sys.exit(app.exec_())

