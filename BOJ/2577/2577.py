a = int(input())
b = int(input())
c = int(input())

count = [0 for _ in range(10)]

num = a * b * c

while num > 0:
    count[num % 10] += 1
    num //= 10

for c in count:
    print(c)