n, m = map(int, input().split())
cards = list(map(int, input().split()))

result_sum = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            cards_sum = cards[i] + cards[j] + cards[k]
            if result_sum < cards_sum <= m:
                result_sum = cards_sum

print(result_sum)