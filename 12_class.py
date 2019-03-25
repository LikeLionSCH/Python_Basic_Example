'''간단한 사칙연산 정수 계산기 클래스
is_set_data() : 정수 데이터 설정 확인 함수
set_data()    : 정수 데이터 설정 함수
add()         : 정수 데이터 덧셈 함수
sub()         : 정수 데이터 뺄셈 함수
mul()         : 정수 데이터 곱셈 함수
div()         : 정수 데이터 나눗셈 함수
'''
class Calculator:
    '''클래스 초기화 함수
    반환 값 : 없음
    인자    : 없음
    기능    : 변수 a, b, None으로 초기화
    '''
    def __init__(self):
        self.a = None
        self.b = None

    '''데이터 설정 확인 함수
    반환 값 : boolean
    인자    : 없음
    기능    : 변수 a, b의 값 설정 확인
    '''
    def is_set_data(self):
        if self.a is not None \
                and self.b is not None:
            return True

        return False

    '''데이터 설정 함수
    반환 값 : 없음
    인자    : 설정 할 정수 값 2개
    기능    : 변수 a, b의 데이터 설정
    '''
    def set_data(self, a, b):
        self.a = a
        self.b = b

    '''계산기 덧셈 함수
    반환 값 : int or str
    인자    : 없음
    기능    : 두 개의 정수의 합을 반환
              데이터 미설정 시 에러 메시지 반환
    '''
    def add(self):
        if self.is_set_data():
            return self.a + self.b

        return "데이터를 먼저 설정해 주세요"

    '''계산기 뺄셈 함수
    반환 값 : int or str
    인자    : 없음
    기능    : 두 개의 정수의 차를 반환
              데이터 미설정 시 에러 메시지 반환
    '''
    def sub(self):
        if self.is_set_data():
            return self.a - self.b

        return "데이터를 먼저 설정해 주세요"

    '''계산기 곱셈 함수
    반환 값 : int or str
    인자    : 없음
    기능    : 두 개의 정수의 곱을 반환
              데이터 미설정 시 에러 메시지 반환
    '''
    def mul(self):
        if self.is_set_data():
            return self.a * self.b

        return "데이터를 먼저 설정해 주세요"

    '''계산기 나눗셈 함수
    반환 값 : float or str
    인자    : 없음
    기능    : 두 개의 정수를 나눈값 반환
              데이터 미설정 시 에러 메시지 반환
    '''
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
