'''함수 예제 1
Hello World! 원하는 만큼 출력하기

함수 사용 이유 : 반복의 제거
'''

def print_hello_world(num):
    for i in range(num):
        print("Hello World!")

print_hello_world(10) # Hello World!가 10번 출력된다.

'''함수 예제 2
두 개의 값을 더하는 함수
'''

def add(a, b):
    return a + b

print(add(10, 5)) # 15
print(add("Hello", " World!")) # Hello World!

'''문제)
1부터 n까지의 정수의 합을 구하는
함수를 작성하세요.
인자로는 하나의 정수값을 받습니다self.
'''

def get_sum(num):
    sum = 0

    for i in range(num + 1):
        sum += i

    return sum

print(get_sum(100)) # 5050

'''함수 내부 변수의 유효 범위
일반적으로 내부에 선언된 변수는
함수 내부에서만 사용가능하다.
'''

def scope_example():
    a = 10
    print("This is Test Function.")

scope_example() # This is Test Function.
# print(a) 에러 발생

'''문제)
사람의 이름과 나이를 출력하는 함수를 만드세요.
함수의 인자로는 사람의 이름과 나이를 받습니다.
'''

def info(name, age):
    print("이름 :", name, "나이 :", age)

info("김민수", 22) # 이름 : 김민수 나이 : 22
