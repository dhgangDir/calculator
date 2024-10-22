# ch 6.2.2 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self): # calculate 메서드 추가. 내용은 추후에 작성
        pass

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.view.activateMessage)
        self.view.btn2.clicked.connect(self.view.clearMessage)