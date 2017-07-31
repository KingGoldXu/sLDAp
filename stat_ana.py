from __future__ import print_function, division

nums = list()
with open('data/jdt_t.txt') as f:
    for a in f:
        x = eval(a)
        nums.append(int(x['tc']))

nums.sort()
print(nums)
print(nums[:len(nums)//3])
print(nums[len(nums)//3:-len(nums)//3])
print(nums[-len(nums)//3:])