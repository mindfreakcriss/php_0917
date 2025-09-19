# 反转数字
def reverse_three(number):
    """Reverses a three-digit integer.

    Args:
        number (int): A three-digit integer.

    Returns:
        int: The reversed integer.
    """
    if not (100 <= number <= 999):
        raise ValueError("Input must be a three-digit integer.")

    hundreds = number // 100  #地板除，想下取只整
    tens = (number // 10) % 10
    units = number % 10

    reversed_number = units * 100 + tens * 10 + hundreds
    return reversed_number

# 合并2个升序数组
def merge_array(arr1, arr2):
    """Merges two arrays into one.

    Args:
        arr1 (list): The first array.
        arr2 (list): The second array.

    Returns:
        list: The merged array.
    """
    # 减少循环次数
    if len(arr2) > len(arr1):
        arr1, arr2 = arr2, arr1

    for index in range(len(arr2)):
        compare = arr1[index:]

        flag = False
        for item in compare:
            if arr2[index] <= item:
                arr1.insert(arr1.index(item), arr2[index])
                flag = True
                break
        if not flag:
            arr1.append(arr2[index])
    return arr1


def reverse_string(s, offset = 0):
    """Reverses a string.

    Args:
        s (str): The input string.

    Returns:
        str: The reversed string.
    """

    # Split the string into two parts
    length = len(s) - offset
    part1 = s[:length]
    part2 = s[length:]
    return   part2 + part1

def binary_search(arr, target):
    """Performs binary search on a sorted array.

    Args:
        arr (list): A sorted array.
        target (int): The target value to search for.

    Returns:
        int: The index of the target value if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoid potential overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def find_next_large_number(arr1, arr2):
    result = []
    for item in arr1:
        flag = False
        for index in range(len(arr2)):
            if arr2[index] == item:
                # 下一个更大的数字
                compare = arr2[index+1:]
                for num in compare:
                    if num > item:
                        result.append(num)
                        flag = True
                        break
        if not flag:
            result.append(-1)
    return result

#  找出数组中只出现一次的数字
def find_number(array):
    temp = {}
    result = []
    for item in array:
        if item in temp:
            temp[item] += 1
        else:
            temp[item] = 1
    for key, value in temp.items():
        if value != 2:
            result.append(key)

    return result

# 判断两个字符串是否为数字孪生
def find_number_twins(s, t):
    s_1 = []
    s_2 = []
    t_1 = []
    t_2 = []
    for index in range(len(s)):
        if index % 2 == 0:
            s_2.append(s[index])
        else:
            s_1.append(s[index])

    for index in range(len(t)):
        if index % 2 == 0:
            t_2.append(t[index])
        else:
            t_1.append(t[index])

    if sorted(s_1) == sorted(t_1) and sorted(s_2) == sorted(t_2):
        return True
    return False

def data_mix(array):
    length = len(array)
    array_b = [0] * length
    for index in range(length):
        temp = array[0:index] + array[index+1:length]
        sum = 1
        for i in range(len(temp)):
            sum *= temp[i]

        array_b[index] = sum
    return array_b

def answer(A):
    length , B = len(A), []
    f = [0 for i in range(length + 1)]
    f[length] = 1
    print(f)
    for i in range(length -1, 0, -1):
        print(i)
        f[i] = f[i+1] * A[i]

    print(f)
    tmp = 1
    for i in range(length):
        B.append(tmp * f[i + 1])
        tmp *= A[i]
    return B

def count_line(array, s):
    row = 1
    last = 0
    for key in range(len(s)):
        last += array[key]
        if last > 100:
            last = last - 100
            row += 1
    # 最后如果last 为100，则占满1行
    if last == 100:
        last = 0
    return [row,last]




if __name__ == "__main__":

    width = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
    S = "abcdefghijklmnopqrst"
    print(count_line(width, S))

    # out_put(10)
    # Example usage
    #num = 900
    #print(f"The reverse of {num} is {reverse_three(num)}")
    # arr1 = [1,3]
    # arr2 = [2,4,5,7]
    # print(f"Merged array: {merge_array(arr1, arr2)}")
    # s = "abcdefg"
    # print(f"Reversed string: {reverse_string(s, 2)}")
    # nums1 = [4,1,2]
    # num2 = [1,3,4,2]
    # print(find_next_large_number(nums1, num2))
    # a = [1,2,5,5,6,6]
    # print(find_number(a))
    # s = "abcd"
    # t = "cdab"
    # print(find_number_twins(s, t))
    # s = "abcd"
    # t = "bcda"
    # print(find_number_twins(s, t))
    # array = [2,4,6]
    # print(data_mix(array))
    # A = [1,2,3,4]
    # B = answer(A)
    # print(B)