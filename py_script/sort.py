# -*- coding: utf-8 -*-
# 插入排序
# 按照扑克牌一样，每次从未排序的牌中抽出一张，插入到已排序的牌中的适当位置，直到所有牌都排序完毕。
# 选出一张牌需要循环全部数据一次 i ，然后和左边的数据进行比较，还需要循环左边的一次 j 次
def insert_sort(nums):
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] < nums[j]:
                nums.insert(j, nums.pop(i))
                break
    return nums

# 选择排序，每次从未排序的牌中选出最小的，放到已排序的牌的末尾，直到所有牌都排序完毕。
def select_sort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums

# 冒泡排序，每次比较相邻的两个元素，如果顺序错误就交换，直到所有元素有序。
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

# 快速排序，选择一个基准元素，将数组分成两部分，一部分比基准元素小，另一部分比基准元素大，然后递归地对这两部分进行排序。
def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 桶排序
def tree_sort(nums):
    countn = [0] * (len(nums)+1)
    result = []
    for i in nums:
        countn[i] += 1 #放入桶里面
    for i in range(1, len(countn)):
        if countn[i] != 0:
            result += [i] * countn[i]
    return result

# 希尔排序，先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录“基本有序”时，再对全体记录进行依次直接插入排序。
def shell_sort(nums):
    step = len(nums) // 2
    while step > 0:
        for i in range(step, len(nums)): #按照步数进行插入排序
            j = i
            while j >= step and nums[j - step] > nums[j]:
                nums[j], nums[j - step] = nums[j - step], nums[j]
                j -= step
        step //= 2
    return nums

# 堆排序

# 初始化一个大顶堆，堆的话，按照数组下标来存储，首个元素为0 ，不存数据，然后从左往右开始计算
# 从根节点开始，把父节点的值和子节点的值进行比较，如果父节点小于子节点，则交换
# 初始化堆之后，把最大元素放到堆尾元素交换，并且把最大值删除，次数堆大小减1，得到最大元素
# 父节点下标为n时，左子节点下标为2n，右子节点下标为2n+1
def Heapify(start, end):
    father = start 
    son = father * 2 # 左子节点
    while son <= end:
        if son + 1 <= end and nums[son] < nums[son + 1]:
            # 右子节点大于左子节点
            son += 1
        if nums[father] < nums[son]: # 父节点小于子节点交换
            nums[father], nums[son] = nums[son], nums[father]
            father = son
            son = father * 2
        else:
            return

def heap_init(nums):
    nums.insert(0,0) # 堆的第一个元素不存数据
    for i in range((len(nums)-1)//2, 0, -1): # 从最后一个非叶子节点开始
        Heapify(i, len(nums)-1)
    return nums

def heap_sort(nums):
    nums = heap_init(nums)
    print("Heap:", nums)
    for i in range(len(nums)-1, 0, -1):
        nums[1], nums[i] = nums[i], nums[1]
        Heapify(1, i-1)
    return nums[1:]

if __name__ == "__main__":
    nums = [5,3,6,4,1,2,8,7]
    #sorted_nums = insert_sort(nums)
    #sorted_nums = select_sort(nums)
    #sorted_nums = bubble_sort(nums)
    #sorted_nums = quick_sort(nums)
    #sorted_nums = tree_sort(nums)
    #sorted_nums = shell_sort(nums)
    sorted_nums = heap_sort(nums)
    print("Sorted array:", sorted_nums)