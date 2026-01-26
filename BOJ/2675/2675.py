t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)

    for ch in s:
        for _ in range(r):
            print(ch, end="")
    print()