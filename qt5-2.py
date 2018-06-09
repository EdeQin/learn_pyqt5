#教程来自 http://code.py40.com/2004.html
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
    QVBoxLayout, QApplication,QGridLayout,QPushButton)

class Qt5_2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):                            #布局问题:https://blog.csdn.net/zhulove86/article/details/52563298
        mainlayout = QVBoxLayout()
        lcd = QLCDNumber(self)  # LCD数字显示
        #sld = QSlider(Qt.Horizontal, self)  # 水平滑动

        screen = QVBoxLayout()  # 垂直布局，对应QHBoxLayout水平布局
        screen.addWidget(lcd)
        #vbox.addWidget(sld)
        #sld.valueChanged.connect(lcd.display)
        grid = QGridLayout()
        mainlayout.addLayout(screen)
        mainlayout.addLayout(grid)         #screen和grid前后是有差别的

        self.setLayout(mainlayout)  # self.xxx设置最基本的布局
        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']
        positions = [(i, j) for i in range(5) for j in range(4)]
        for name, position in zip(names, positions):
            if name == '':
                continue
            else:
                button = QPushButton(name)
                grid.addWidget(button, *position)

        self.setGeometry(300, 300, 250, 350)
        self.setWindowTitle('计算器')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Qt5_2()
    sys.exit(app.exec_())
