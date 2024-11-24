import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow


# 窗口对象
class MyForm(QMainWindow):
    firstvalue = 0
    secondvalue = 0
    # 行为
    action = ""

    def __init__(self, parent=None):
        # 创建窗口对象？？
        QtWidgets.QWidget.__init__(self, parent)
        # 加载ui文件？？加载了这个文件后，是不是意味着窗口对象已经创建？？
        uic.loadUi("calculator_ui.ui", self)

        # self指的是该类的实例对象，然后去调用按钮对象，的方法，参数是鼠标点击了这个按钮
        # 这表示调用这个实例对象的方法吗？
        self.button_1.clicked.connect(self.buttonClicked)
        self.button_2.clicked.connect(self.buttonClicked)
        self.button_3.clicked.connect(self.buttonClicked)
        self.button_4.clicked.connect(self.buttonClicked)
        self.button_5.clicked.connect(self.buttonClicked)
        self.button_6.clicked.connect(self.buttonClicked)
        self.button_7.clicked.connect(self.buttonClicked)
        self.button_8.clicked.connect(self.buttonClicked)
        self.button_9.clicked.connect(self.buttonClicked)
        self.button_0.clicked.connect(self.buttonClicked)

        self.button_plus.clicked.connect(self.action_button)  # 加
        self.button_minus.clicked.connect(self.action_button)  # 减
        self.button_multi.clicked.connect(self.action_button)  # 乘
        self.button_division.clicked.connect(self.action_button)  # 除
        self.button_equal.clicked.connect(self.result)  # 等于
        self.button_C.clicked.connect(self.clean)  # 清空
        self.button_comma.clicked.connect(self.buttonClicked)  # 点
        self.button_bksp.clicked.connect(self.backspace)  # 上一步

    def buttonClicked(self):
        # 等号按钮没有处于激活状态
        if self.button_equal.isEnabled() == False:
            self.lcdNumber.display(0)
            # 启用等号按钮
            self.button_equal.setEnabled(True)
        # 槽函数，返回触发当前槽函数的对象
        sender = self.sender()
        # 得到显示框当前显示的值
        x = str(self.lcdNumber.value())
        # 确保当前数字小数点只有一个
        if self.button_comma.isEnabled() == True:
            x = x[:-2]
            if sender.text() == ".":
                x += sender.text()
                self.button_comma.setEnabled(False)
            else:
                if x == "0":
                    x = sender.text()
                else:
                    x += sender.text()
        else:
            if self.button_comma.isChecked() == True:
                self.button_comma.setCheckable(False)
                x = x[:-1] + sender.text()
            else:
                x += sender.text()
        if len(x) > 7:
            self.lcdNumber.setDigitCount(len(x))
        # 显示器显示字符串x
        self.lcdNumber.display(x)

    def action_button(self):
        global firstvalue, action
        sender = self.sender()
        firstvalue = self.lcdNumber.value()
        self.lcdNumber.display(0)
        action = sender.text()
        self.button_comma.setEnabled(True)
        self.button_comma.setCheckable(True)
        self.lcdNumber.setDigitCount(7)

    def result(self):
        global firstvalue, secondvalue, action
        secondvalue = self.lcdNumber.value()
        if action == "+":
            x = firstvalue + secondvalue
        if action == "-":
            x = firstvalue - secondvalue
        if action == "*":
            x = firstvalue * secondvalue
        if action == "/":
            x = firstvalue / secondvalue
        x = str(x)
        if len(x) - x.index(".") > 3:
            y = len(x) - x.index(".") - 3
            x = x[:-y]
        if x.endswith(".0"):
            x = x[:-2]
        if len(x) > 7:
            self.lcdNumber.setDigitCount(len(x))
        self.lcdNumber.display(x)
        firstvalue = 0
        secondvalue = 0
        action = ""
        self.button_comma.setEnabled(True)
        self.button_comma.setCheckable(True)
        self.button_equal.setEnabled(False)

    # 删除全部
    def clean(self):
        global firstvalue, secondvalue, action
        self.lcdNumber.display(0)
        firstvalue = 0
        secondvalue = 0
        action = ""
        self.button_comma.setEnabled(True)
        # 按钮点击后，会持续保持一种状态
        self.button_comma.setCheckable(True)
        # 限制显示器的显示位数
        self.lcdNumber.setDigitCount(7)

    # 后退操作
    def backspace(self):
        x = str(self.lcdNumber.value())
        if self.button_comma.isEnabled() == True:
            x = x[:-3]
        else:
            x = x[:-1]
        if len(x) > 7:
            self.lcdNumber.setDigitCount(len(x))
        else:
            self.lcdNumber.setDigitCount(7)
        self.lcdNumber.display(x)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyForm()
    window.show()
    sys.exit(app.exec())
