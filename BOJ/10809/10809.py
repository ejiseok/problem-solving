s = input()

result = [-1 for _ in range(26)]

for i in range(len(s)):
    if result[ord(s[i]) - ord('a')] == -1:
        result[ord(s[i]) - ord('a')] = i

for pos in result:
    print(pos, end=" ")
print()