# ch 4.2.4 main.py
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox, QPlainTextEdit, QHBoxLayout)
from PyQt5.QtGui import QIcon

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit() # 텍스트 에디트 위젯 생성
        self.te1.setReadOnly(True) # 텍스트 에디트 위젯을 읽기만 가능하도록 수정

        self.btn1 = QPushButton('Message', self) # 버튼 추가
        self.btn1.clicked.connect(self.activateMessage) # 버튼 추가시 핸들러 함수 연결

        self.btn2 = QPushButton('Clear', self) # 버튼 2 추가
        self.btn2.clicked.connect(self.clearMessage) # 버튼 2 핸들러 함수 연결

        hbox = QHBoxLayout() # 수평 레이아웃 위젯 생성 버튼 1, 2 추가
        hbox.addStretch(1) # 빈 공간
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2) # 버튼 위치
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox) # btn1 위치에 hbox 배치
        vbox.addStretch(1)

        self.setLayout(vbox) # 빈 공간 - 버튼 - 빈 공간 순으로 수직 배치된  레이아웃 설정

        self.setWindowTitle('Calculator')
        self.resize(256, 256)
        self.show()

    def activateMessage(self): # 핸들러 함수 수정 : 메시지가 텍스트 에디트에 출력되도록
        # QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        self.te1.clear()

if __name__=='__main__':
    app = QApplication(sys.argv)
    view = Calculator()
    sys.exit(app.exec_())