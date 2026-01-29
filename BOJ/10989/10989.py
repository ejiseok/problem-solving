import sys

n = int(input())

count_num = [0 for _ in range(10001)]

for i in range(n):
    input_num = int(sys.stdin.readline())
    count_num[input_num] += 1

for i in range(len(count_num)):
    for j in range(count_num[i]):
        print(i)