'''
Author: sunke 375352086@qq.com
Date: 2024-11-21 15:06:31
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-21 15:19:38
FilePath: /PyQT_Practice/BasicTreeWidget.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
树控件(QTreeWidget)的基本用法
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QBrush,QColor
from PyQt5.QtCore import Qt

class BasicTreeWidget(QMainWindow):
    def __init__(self,parent= None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件(QTreeWidget)的基本用法')
        self.resize(600,300)


        # 创建树控件
        self.tree = QTreeWidget()
        # 将树控件设为中心控件，充满整个屏幕
        self.setCentralWidget(self.tree)

        # 为树控件指定列数    让它显示两列
        # 每个都只能显示两列
        self.tree.setColumnCount(3)

        # 指定列标签
        self.tree.setHeaderLabels(['key','Value','dd'])

        # 根节点
        # 类似于表格的创建字段
        root = QTreeWidgetItem(self.tree)
        # 将根阶段放置在第一列
        root.setText(0,'根节点')
        # 给根节点设置图标
        root.setIcon(0,QIcon('/Users/sunke/Downloads/Code_Practice/untitled folder/000.jpg'))
        # 给第一列设置列宽
        self.tree.setColumnWidth(0,160)

        # 添加子节点1
        # 让子节点child1指向root
        child1 = QTreeWidgetItem(root)
        # 设置子节点第一列文本
        child1.setText(0,'子节点1')
        # 设置子节点第二列的文本
        child1.setText(1,"子节点1的数据")

        child1.setText(2,"子节点1的hh")
        # 设置子节点第一列的图标
        child1.setIcon(0,QIcon('/Users/sunke/Downloads/Code_Practice/untitled folder/001.jpg'))
        # 给子节点第一列添加复选框
        child1.setCheckState(0,Qt.PartiallyChecked)
        # 设置子节点第二列的图标
        child1.setIcon(1, QIcon('/Users/sunke/Downloads/Code_Practice/untitled folder/002.jpg'))


        # 添加子节点2
        # 让子节点child2指向root
        child2 = QTreeWidgetItem(root)
        # 设置子节点第一列文本
        child2.setText(0,'子节点2')
        # 设置子节点第一列设置图标
        child2.setIcon(0,QIcon('/Users/sunke/Downloads/Code_Practice/untitled folder/003.jpg'))

        # 为子节点2再添加一个子节点
        # 让子节点chil2_指向子节点chil2
        child2_ = QTreeWidgetItem(child2)
        # 设置子节点第一列文本
        child2_.setText(0,'子节点2的子节点的第一列')
        # 设置子节点第一列文本
        child2_.setText(1, '子节点2的子节点的第二列')
        # 设置子节点第一列文本    由于设置了self.tree.setColumnCount(2)，所以没有第三列
        # child2_.setText(2, '子节点2的子节点的第三列')
        # 给子节点的第一列设置图标
        child2_.setIcon(0,QIcon('/Users/sunke/Downloads/Code_Practice/untitled folder/004.jpg'))
        # 给子节点的第二列设置图标
        child2_.setIcon(1, QIcon('/Users/sunke/Downloads/Code_Practice/untitled folder/005.jpg'))

        # 将节点默认展开
        self.tree.collapseAll()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())
