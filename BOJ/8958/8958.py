t = int(input())

for _ in range(t):
    result = input()
    final_score = 0

    score = 0
    for c in result:
        if c == "O":
            score += 1
            final_score += score
        else:
            score = 0

    print(final_score)
