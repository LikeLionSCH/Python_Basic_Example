class Calculator:
    def __init__(self):
        self.a = None
        self.b = None

    def is_set_data(self):
        if self.a is not None \
                and self.b is not None:
            return True

        return False

    def set_data(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        if self.is_set_data():
            return self.a + self.b

        return "데이터를 먼저 설정해 주세요"

    def sub(self):
        if self.is_set_data():
            return self.a - self.b

        return "데이터를 먼저 설정해 주세요"

    def mul(self):
        if self.is_set_data():
            return self.a * self.b

        return "데이터를 먼저 설정해 주세요"

    def div(self):
        if self.is_set_data():
            return self.a / self.b

        return "데이터를 먼저 설정해 주세요"


calc = Calculator()  # 계산기 객체 선언

print(calc.a, calc.b, calc.is_set_data())  # 데이터를 설정하지 않은 계산기 객체 확인

calc.set_data(10, 5)  # 계산기 객체 데이터 설정
print(calc.a, calc.b, calc.is_set_data())  # 데이터 설정 후 계산기 객체 확이

print(calc.a, "+", calc.b, "=", calc.add())  # 계산기 객체 덧셈 함수 호출
print(calc.a, "-", calc.b, "=", calc.sub())  # 계산기 객체 뺄셈 함수 호출
print(calc.a, "*", calc.b, "=", calc.mul())  # 계산기 객체 곱셈 함수 호출
print(calc.a, "//", calc.b, "=", calc.div())  # 계산기 객체 나눗셈 함수 호출

no_data_calc = Calculator()  # 데이터를 설정하지 않을 계산기 객체 선언

print(no_data_calc.a, "+", no_data_calc.b, "=", no_data_calc.add())  # 데이터 설정이 안된 계산기 객체 덧셈 함수 사용
print(no_data_calc.a, "-", no_data_calc.b, "=", no_data_calc.sub())  # 데이터 설정이 안된 계산기 객체 뺄셈 함수 사용
print(no_data_calc.a, "*", no_data_calc.b, "=", no_data_calc.mul())  # 데이터 설정이 안된 계산기 객체 곱셈 함수 사용
print(no_data_calc.a, "//", no_data_calc.b, "=", no_data_calc.div())  # 데이터 설정이 안된 계산기 객체 나눗셈 함수 사용
