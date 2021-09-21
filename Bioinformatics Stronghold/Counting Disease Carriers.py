from math import sqrt

nums = '0.1 0.25 0.5'
nums = list(map(float, nums.split()))

res = [2*sqrt(i)-i for i in nums]
rounds = [round(num, 3) for num in res]

print(*rounds, sep = ' ')
