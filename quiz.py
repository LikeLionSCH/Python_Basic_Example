
'''
Loop, Condition
첫 줄에 정수의 입력값이 주어진다. (0 < N < 10)

그 다음 N번 째 줄에 다음과 같이 출력한다.
입력
9

출력
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
 2 4 6 8
1 3 5 7 9
'''

N = int(input())

# Solution 1 - Using double loop
for i in range(1, N+1):
    for j in range(1, N+1):
        if i % 2 != 0:
            if j % 2 != 0 :
                print(j, end="")

            else:
                print(" ", end="")

        else:
            if j % 2 != 0:
                print(" ", end="")

            else:
                print(j, end="")

    print()

# Solution 2 - Using join in one line
print('\n'.join(''.join(str(i) if i%2 == j%2 else ' ' for i in range(1, N+1)) for j in range(1, N+1)))

# Solution 3 - Using join & List comprehension
arr = [['' if x % 2 != y % 2 else str(x + 1) for x in range(N)] for y in range(N)]

for el in arr:
    print(' '.join(el))
