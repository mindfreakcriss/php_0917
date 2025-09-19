# bubble sort and selection sort implementations
def bubble_sort(array):
    for item in range(len(array)-1, 0, -1):
        for i in range(item):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    return array

array = [64, 34, 25, 12, 22, 11, 90]
sorted_array = bubble_sort(array)
print("Sorted array is:", sorted_array)

# Selection Sort
def select_sort(array):
    for item in range(len(array)):
        min_index = item
        for j in range(item+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[item], array[min_index] = array[min_index], array[item]
    return array

array = [64, 25, 12, 22, 11]
sorted_array = select_sort(array)
print("Sorted array is:", sorted_array)

def insert_sort(array):
    for item in range(1, len(array)):
        key = array[item]
        j = item - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

array = [12, 11, 13, 5, 6]
sorted_array = insert_sort(array)
print("Sorted array is:", sorted_array)

# own average function
def get_own_avg(array):
    sum = 0
    length = 0
    for item in range(len(array)):
        if array[item] % 2 == 0:
            sum += array[item]
            length += 1
    return sum / length if length > 0 else 0

array = [1, 2, 3, 4, 5, 6]
average = get_own_avg(array)
print("Average of even numbers is:", average)

# palindrome check function
def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
s = "racecar"
result = is_palindrome(s)
print(f"{s} is a palindrome: {result}")

def countdown(number):
    if number >= 0:
        print("Blastoff! %s" % number)
        countdown(number - 1)

countdown(10)


def say_list(params):
    if params:
        if type(params[0]).__name__ == 'list':
            say_list(params[0])
        else:
            print(params[0])
        say_list(params[1:])


# say_list([
#     1,
#     2,
#     3,
#     [ 4, 5, 6],
#     7,
#     [8,
#          [9,10,11,
#             [12,13,14]
#          ]
#     ],
#     [15,16,17,18,19,
#      [20,21,22,
#       [23,24,25,
#           [26,27,28,29
#           ],30,31
#       ],32
#       ],33]]
# )

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse(s[:-1])

s = "Hello, World!"
reversed_s = reverse(s)
print("Reversed string is:", reversed_s)


def count_x(string):
    if len(string) == 0:
        return 0
    elif string[0] == 'x':
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])

string = "xaxbxcxdx"
count = count_x(string)
print(f"Number of 'x' in '{string}': {count}")


def count_length(string):
    if len(string) == 1:
        return len(string[0])
    else:
        return len(string[0]) + count_length(string[1:])

string = ["ab","c","def","ghij"]
length = count_length(string)
print(f"Length of '{string}': {length}")

#  递归 增加记忆化处理重复子问题
#  自下而上处理递归问题
#
def fib(n):
    if n == 0:
        return 0
    a = 0
    b = 1

    for i in range(1, n):
        temp = a
        a = b
        b = temp + a
    return b

n = 10
result = fib(n)
print(f"The {n}th Fibonacci number is: {result}")

def quick_sort(array):



