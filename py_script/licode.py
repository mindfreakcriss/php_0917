# coding=utf-8

# 暴力枚举
# def fun1(nums, target):
#     for i in range(len(nums)):
#         temp = target - nums[i]
#         for j in range(len(nums)):
#             if j != i and nums[j] == temp:
#                 return [i, j]

# hash 表
def fun1(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        temp = target - num
        if temp in hashmap:
            return [hashmap[temp], i]
        hashmap[num] = i

if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    # nums = [3,2,4]
    # target = 6
    # nums = [3,3]
    # target = 6
    nums = [-1,-2,-3,-4,-5]
    target = -8
    print(fun1(nums, target))