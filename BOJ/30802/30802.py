n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

pairs_t = 0
for size in sizes:
    pairs_t += size // t + (1 if size % t != 0 else 0)

pairs_p = n // p
each_p = n % p

print(pairs_t)
print(pairs_p, each_p)