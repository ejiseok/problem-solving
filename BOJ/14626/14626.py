isbn = input()

isbn_sum = 0
is_three_times_weight = False

for i in range(len(isbn)):
    if isbn[i] == "*":
        is_three_times_weight = True if i % 2 == 1 else False
        continue

    isbn_sum += int(isbn[i]) * (3 if i % 2 == 1 else 1)

for i in range(10):
    if (isbn_sum + (3 * i if is_three_times_weight else i)) % 10 == 0:
        print(i)
        break