'''
Author: sunke 375352086@qq.com
Date: 2024-11-22 15:53:08
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-22 15:53:17
FilePath: /PyQT_Practice/LocalHTML.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
装在本地Web页面
"""

import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class WebEngineView(QMainWindow):
    def __init__(self):
        super(WebEngineView, self).__init__()
        self.setWindowTitle("装载本地Web页面")
        self.setGeometry(50,50,1355,730)
        url = os.getcwd() + '/test.html'
        self.browser =  QWebEngineView()
        self.browser.load(QUrl.fromLocalFile(url))

        self.setCentralWidget(self.browser)
        print(os.getcwd())

if __name__ == '__main__':
    app =    QApplication(sys.argv)
    demo = WebEngineView()
    demo.show()
    sys.exit(app.exec_())
