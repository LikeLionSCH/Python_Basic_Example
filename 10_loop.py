'''while Loop
기본 구조

while 조건문:
    실행할 문장1
    실행할 문장 2
'''

res = 0
i = 0

while i <= 10:
    res += i
    i += 1

print(res) # 55

'''for loop
기본 구조

for _ in 리스트(튜플, 문자열):
    수행할 문장1
    수행할 문장2
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = 0

for i in arr:
    res += i

print(res) # 55

'''range()함수
수열을 생성해주는 기능
range(시작, 끝 + 1, 간격)의 형식
시작위치에 값을 넣지 않으면 기본 설정값 0
간격위치에 값을 넣지 않으면 기본 설정값 1

len() 함수
반복 가능한 자료형의 길이를 반환
'''

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = 0

for i in range(len(arr)):
    res += arr[i]

print(res) # 55

for i in range(10):
    print(i, end=" ")

print() # 0 1 2 3 4 5 6 7 8 9

for i in range(2, 10):
    print(i, end=" ")

print() # 2 3 4 5 6 7 8 9

for i in range(1, 20, 3):
    print(i, end=" ")

print() # 1 4 7 10 13 16 19

'''1부터 10까지의 수의 합 구하기
range()함수 응용
'''

res = 0

for i in range(11):
    res += i

print(res) # 55

'''문제)
1부터 100까지의 정수의 합을 구하시오.
'''

# 해결 방법 1
arr = [i for i in range(101)]
res = 0

for i in arr:
    res += i

print(res) # 5050

# 해결 방법 2
res = 0

for i in range(101):
    res += i

print(res) # 5050

# 해결 방법 3
print(sum([x for x in range(101)])) # 5050

# 해결 방법 4
print(sum(range(101))) # 5050

'''문제)
1부터 100까지의 소수를 출력하세요.
'''

for i in range(2, 101):
    check = True

    for j in range(2, i):
        if i % j == 0:
            check = False
            break

    if check:
        print(i, end=" ")

print()
