nums = list(map(int, input().split()))
nums = [n * n for n in nums]
print(sum(nums) % 10)