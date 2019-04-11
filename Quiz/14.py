title = '''
구구단 프로그램을 실행합니다.
1. 홀수 구구단
2. 짝수 구구단
3. 종료
'''

def gugudan_odd():
    for i in range(1, 10):
        if i % 2 != 0:
            print("\n%d단" % i)

            for j in range(1, 10):
                print("%d * %d = %d" % (i, j, i * j))

def gugudan_even():
    for i in range(1, 10):
        if i % 2 == 0:
            print("\n%d단" % i)

            for j in range(1, 10):
                print("%d * %d = %d" % (i, j, i * j))


while True:
    print(title)

    num = int(input("숫자를 입력하세요 : "))

    if num == 1:
        gugudan_odd()

    elif num == 2:
        gugudan_even()

    elif num == 3:
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못 입력했습니다. 1 ~ 3의 숫자를 입력하세요.")
