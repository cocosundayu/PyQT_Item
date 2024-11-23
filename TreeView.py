'''
Author: sunke 375352086@qq.com
Date: 2024-11-21 16:03:20
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-21 16:03:29
FilePath: /PyQT_Practice/TreeView.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
QTreeView控件与系统定制模式

与QTreeWidget的不同点： QTreeWiget装载数据的方式是通过Model,比如Model里面的QDirModel 用来显示当前操作系统的目录结构
QTreeView  一般用于比较复杂的树
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 创建QDirModel控件
    model = QDirModel()
    # 创建QTreeView控件
    tree = QTreeView()
    # 设置model
    tree.setModel(model)

    # 把树作为一个窗口
    tree.setWindowTitle('QTreeView')
    # 设置树窗口的尺寸
    tree.resize(600,400)
    # 显示树
    tree.show()
    sys.exit(app.exec_())


