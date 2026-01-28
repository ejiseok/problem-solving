while True:
    num = input()

    if num == "0":
        break

    is_pal = True
    for i in range(len(num) // 2):
        if num[i] != num[len(num) - 1 - i]:
            is_pal = False
            break

    if is_pal:
        print("yes")
    else:
        print("no")