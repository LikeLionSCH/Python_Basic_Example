N = int(input())

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i % 2 != 0:
            if j % 2 != 0:
                print(j, end="")

            else:
                print(" ", end="")

        else:
            if j % 2 != 0:
                print(" ", end="")

            else:
                print(j, end="")

    print()

print('\n'.join(''.join(str(i) if i % 2 == j % 2 else ' ' for i in range(1, N+1))
                for j in range(1, N+1)))

arr = [[' ' if x % 2 != y % 2 else str(x + 1) for x in range(N)] for y in range(N)]

for el in arr:
    print(' '.join(el))
