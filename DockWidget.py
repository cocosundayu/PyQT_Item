'''
Author: sunke 375352086@qq.com
Date: 2024-11-21 16:28:12
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-21 16:57:49
FilePath: /PyQT_Practice/DockWidget.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
停靠控件 (QDockWidget)

这是一个窗口 可以悬浮 可以拖动
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)

        self.setWindowTitle('停靠控件 (QDockWidget)')

        # 水平布局
        layout = QHBoxLayout()
        # 创建停靠控件
        self.items = QDockWidget('Dockable',self)
        # 创建列表控件
        self.listWidget = QListWidget()
        # 为列表控件添加item
        self.listWidget.addItem('item1')
        self.listWidget.addItem('item2')
        self.listWidget.addItem('item3')

        # 将列表控件放到停靠(控件)窗口里面
        self.items.setWidget(self.listWidget)

        layout.addWidget(self.items)
        # 设置中心窗口
        self.setCentralWidget(QLineEdit())
        # 添加停靠窗口  在右侧
        self.addDockWidget(Qt.RightDockWidgetArea,self.items)

        # 默认为停靠状态，可以设置为悬浮
        self.items.setFloating(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = DockDemo()
    demo.show()
    sys.exit(app.exec_())

