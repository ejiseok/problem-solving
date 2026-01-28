n = int(input())
scores = list(map(int, input().split()))

highest = max(scores)
score_sum = 0

for score in scores:
    score_sum += score / highest * 100

print(score_sum / n)