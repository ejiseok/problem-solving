n = int(input())

count = 1
room = 1
inc = 6

while room < n:
    room += inc
    count += 1
    inc += 6

print(count)