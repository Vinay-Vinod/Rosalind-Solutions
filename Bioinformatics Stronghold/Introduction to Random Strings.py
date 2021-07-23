import math

s = 'ACAGCTACGGTGAAACCGTTATTCTCGTTACAGAACTGTTTCTATTGCACCAAATAGCCTTTAAGAAGCCAGATCTTGGGTGCGCGTT'
nums = '0.095 0.131 0.218 0.274 0.324 0.374 0.442 0.484 0.552 0.583 0.636 0.701 0.762 0.781 0.874 0.937'
nums = list(map(float, nums.split()))

at = 0
gc = 0
for x in s:
    if x == 'A' or x == 'T':
        at +=1
    elif x == 'G' or x == 'C':
        gc += 1

probs = []
for i in range(len(nums)):
    probs.append(round(math.log10((((1 - nums[i]) / 2)**at) * (nums[i] / 2) **gc), 3))

print(*probs, sep=' ')
