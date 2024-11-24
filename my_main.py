# 导入所需库
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QTextBrowser


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("untitled.ui", self)
        self.setInitialSize()
        self.textBrowser_now.setText('0')

        self.pushButton_1.clicked.connect(self.buttonClicked)
        self.pushButton_2.clicked.connect(self.buttonClicked)
        self.pushButton_3.clicked.connect(self.buttonClicked)
        self.pushButton_4.clicked.connect(self.buttonClicked)
        self.pushButton_5.clicked.connect(self.buttonClicked)
        self.pushButton_6.clicked.connect(self.buttonClicked)
        self.pushButton_7.clicked.connect(self.buttonClicked)
        self.pushButton_8.clicked.connect(self.buttonClicked)
        self.pushButton_9.clicked.connect(self.buttonClicked)
        self.pushButton_0.clicked.connect(self.buttonClicked)
        self.pushButton_point.clicked.connect(self.buttonClicked)  # 点

        self.pushButton_clean.clicked.connect(self.clean)  # 清空
        self.pushButton_back.clicked.connect(self.backspace)  # 上一步
        self.pushButton_plus.clicked.connect(self.action_button)  # 加
        self.pushButton_minus.clicked.connect(self.action_button)  # 减
        self.pushButton_multi.clicked.connect(self.action_button)  # 乘
        self.pushButton_divide.clicked.connect(self.action_button)  # 除
        self.pushButton_remainer.clicked.connect(self.action_button)  # 取余
        self.pushButton_square.clicked.connect(self.action_button)  # 平方
        self.pushButton_equal.clicked.connect(self.result)  # 等于

    # 数字的输入
    def buttonClicked(self):
        """数字输入到下方的输入框"""
        sender = self.sender()
        new_text = sender.text()
        current_text = self.textBrowser_now.toPlainText()
        text = current_text + new_text
        # 这里需要判断考虑两个条件，输入的是数字[1~9]还是[0]还是[.]，并且好要保证运算数中至多有一个[.]
        # 判断什么是否可以添加元素'.'
        if new_text == '.':
            if '.' not in current_text:
                self.textBrowser_now.setPlainText(text)
        # 判断什么是否可以添加元素'0'
        elif new_text == '0':
            if '.' in current_text:  # 小数
                self.textBrowser_now.setPlainText(text)
            else:  # 整数
                if current_text[0] != '0':
                    self.textBrowser_now.setPlainText(text)
        else:
            if '.' in current_text:
                self.textBrowser_now.setPlainText(text)
            else:
                if current_text[0] != '0':
                    self.textBrowser_now.setPlainText(text)
                else:
                    self.textBrowser_now.setPlainText(new_text)

    # 清零
    def clean(self):
        """这个简单，格式化"""
        self.textBrowser_now.setPlainText('0')
        self.textBrowser_history.clear()

    # 这里的self指的是调用这个方法的对象，也就是QPushButton类的实例对象pushButton_back
    def backspace(self):
        """退回到上一步，下方输入框的内容取[:-1]"""
        if self.textBrowser_now.toPlainText() != '0':
            current_text = self.textBrowser_now.toPlainText()
            self.textBrowser_now.setPlainText(current_text[:-1])
        if self.textBrowser_now.toPlainText() == '':
            self.textBrowser_now.setPlainText('0')

    # 运算符 
    def action_button(self):
        """运算符号，将下方输入框中的数字加上运算符后复制到上方的输入框，下方输入框变为0"""
        """如果上方输入框最后最后一位是运算符，会将其修改"""
        operators = ['÷', '%', '×', '－', '＋']
        sender = self.sender()
        operator = sender.text()

        text_history = self.textBrowser_history.toPlainText()
        text_now = self.textBrowser_now.toPlainText()

        if text_history != '' and text_history[-1] in operators:
            text_history = text_history[:-1]
            text_history = text_history+operator
            self.textBrowser_history.setPlainText(text_history)
        else:
            if operator == 'x²':
                self.textBrowser_history.setPlainText(f'{text_now}²={float(text_now) ** 2}')
                self.textBrowser_now.setPlainText(str(float(text_now) ** 2))
            else:
                self.textBrowser_history.setPlainText(text_now + operator)
                self.textBrowser_now.setPlainText('0')

    def result(self):
        """点击等号，完成运算"""
        text_history = self.textBrowser_history.toPlainText()
        text_now = self.textBrowser_now.toPlainText()
        operators = ['÷', '%', '×', '－', '＋']

        if text_history != '' and text_history[-1] in operators:
            num1 = float(text_history[:-1])
            num2 = float(text_now)
            operator = text_history[-1]
            if operator == '＋':
                result = num1 + num2
            elif operator == '－':
                result = num1 - num2
            elif operator == '×':
                result = num1 * num2
            elif operator == '÷':
                result = num1 / num2
            else:
                result = num1 % num2
            self.textBrowser_history.setText(f'{self.textBrowser_history.toPlainText()}'
                                             f'{self.textBrowser_now.toPlainText()}={str(result)}')
            self.textBrowser_now.setPlainText(str(result))
        else:
            self.textBrowser_history.setPlainText(text_now)
            self.textBrowser_now.setPlainText('0')

    def setInitialSize(self):
        # 设置窗口的初始大小，例如 800x600
        self.setGeometry(1000, 500, 700, 900)  # 参数分别为 x, y, 宽度, 高度
        # 或者使用 resize 方法
        # self.resize(800, 600)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
