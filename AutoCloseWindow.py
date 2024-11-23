'''
Author: sunke 375352086@qq.com
Date: 2024-11-21 17:37:32
LastEditors: sunke 375352086@qq.com
LastEditTime: 2024-11-21 18:56:05
FilePath: /PyQT_Practice/AutoCloseWindow.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
"""
让程序定时关闭

QTimer.singleShot    在指定时间后只调用一次

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


if __name__ == '__main__':
    app = QApplication(sys.argv)

    label =  QLabel("<font color=red size=140><b>Hello World,窗口在5秒后自动关闭！</b></font>")
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint)
    label.show()
    # 设置五秒
    QTimer.singleShot(5000,app.quit)
    sys.exit(app.exec_())
