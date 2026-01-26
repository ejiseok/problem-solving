nums = []
for _ in range(10):
    nums.append(int(input()))

s = set([n % 42 for n in nums])
print(len(s))
