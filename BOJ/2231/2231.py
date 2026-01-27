n = int(input())

for i in range(n // 2, n + 1):
    ctor = i + sum(map(int, str(i)))
    if ctor == n:
        print(i)
        break
else:
    print(0)