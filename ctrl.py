# ch 6.6.7 ctrl.py
class Control:

    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def calculate(self): # calculate 메서드 추가. 내용은 추후에 작성
        num1 = float(self.view.le1.text()) # 첫 번째 라인 에디트에 입력된 숫자 읽어옴
        num2 = float(self.view.le2.text()) # 첫 번째 라인 에디트에 입력된 숫자 읽어옴
        operator = self.view.cb.currentText() # 콤보 박스에 선택된 연산자  확인
        
        if operator == '+':
            return f'{num1} + {num2} = {self.sum(num1, num2)}'
        
        else:
            return 'Calculation Error'
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(lambda: self.view.setDisplay(self.calculate()))
        self.view.btn2.clicked.connect(self.view.clearMessage)
    
    def sum(self, a, b): # 덧셈 함수 추가
        return a + b