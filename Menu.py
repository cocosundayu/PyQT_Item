
'''
Author: sunke 375352086@qq.com
Date: 2024-11-19 19:16:23
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-19 20:40:31
FilePath: /PyQT_Practice/Menu.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
创建和使用菜�?
"""

import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('剪贴板演示')
        # 设置窗口尺寸
        self.resize(300,200)
        # 获取菜单�?
        bar = self.menuBar()

        # 给菜单栏添加 "文件"
        file = bar.addMenu("file")
        # 给文件添加动�? "新建"
        quit=QAction(QIcon('/Users/sunke/Downloads/孙科.jpg'),"Quitzd",self)
        file.addAction(quit)
        # 第一种添加方�?s
        file.addAction("新建")


        # 创建"退�?"动作
        quit =QAction("退出",self)
        # �?"退�?"添加�?"文件"下面
        file.addAction(quit)


        # 第二种添加方�?  通过QAction
        # 添加动作 "保存"
        save = QAction("保存",self)
        # 给保存添加快捷键
        save.setShortcut("Ctrl + S")
        # �?"保存"动作添加�?"文件"下面
        file.addAction(save)

        # 把save触发连接�?
        save.triggered.connect(self.process)

        # 给菜单栏添加"编辑"菜单
        edit = bar.addMenu("Edit")
        # �?"编辑"添加"复制"动作
        edit.addAction("copy")
        edit.addAction("quit")

        # �?"编辑"添加"粘贴"动作
        edit.addAction("paste")


    # 给动作添加事�?
    def process(self,a):
        print(self.sender().text())

# 直接运行此脚本，才会调用下面代码
if __name__ == '__main__':
    # app实例化，并传�?
    app =   QApplication(sys.argv)
    # 创建对象
    main = Menu()
    # 创建窗口
    main.show()
    # 进入主循环，调用exit方法，确保主循环安全退�?
    sys.exit(app.exec_())
