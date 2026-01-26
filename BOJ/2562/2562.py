max_num = int(input())
index = 1

for i in range(2, 10):
    input_num = int(input())
    if input_num > max_num:
        max_num = input_num
        index = i

print(max_num)
print(index)
