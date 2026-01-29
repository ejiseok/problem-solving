t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    apartment = [[] for i in range(15)] # 층 수는 0층부터 있으니, 0에서부터 14층까지의 15층
    apartment[0] = [i for i in range(16)] # 각 층에는 1호부터 있고, 0층의 i호는 i명이 산다, 0호에는 0명으로 지정

    # k층의 전 층까지의 인원수를 계산
    for i in range(1, k + 1):
        apartment[i].append(0) # 0호에는 0명으로 지정
        for j in range(1, n + 1):
            person_sum = apartment[i - 1][j] + apartment[i][j - 1]
            apartment[i].append(person_sum)

    # k층의 n호실까지의 인원수를 계산
    apartment[k].append(0)
    person_sum = 1
    for i in range(1, n + 1):
        apartment[k].append(person_sum)
        person_sum += apartment[k - 1][i]

    print(apartment[k][n])