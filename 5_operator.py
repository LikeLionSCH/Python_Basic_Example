'''수식 연산자
+  덧셈
-  뺄셈
*  곱셈
// 정수형 나눗셈
/  실수형 나눗셈
%  나머지 연산
'''

a, b = 5, 10

print(a + b) # 15
print(a - b) # -5
print(a * b) # 50
print(a // b) # 0
print(a / b) # 0.5
print(a % b) # 5

'''비교 연산자 (True 또는 False)
a == b a와 b가 같은가
a != b a와 b가 다른가
a > b  a가 b보다 큰가
a < b  a가 b보다 작은가
a >= b a가 b보다 크거나 같은가
a <= b a가 b보다 작거나 같은가
'''

a, b = 5, 10

print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True

'''논리 연산자 (True 또는 False)
a and b a와 b모두 True인가
a or b  a와 b 중에 True가 있는가
not b   b를 반대로 바꿔줘
'''

a, b, c = True, False, True

print(a and b) # False
print(a and c) # True
print(a or b) # True
print(b or b) # False
print(not a) # False
print(not b) # True
