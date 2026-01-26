h, m = map(int, input().split())

if m >= 45:
    m -= 45
else:
    m = 60 + (m - 45)
    h = (h - 1) % 24

print(h, m)
