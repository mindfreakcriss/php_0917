# coding=utf-8
import sort

if __name__ == "__main__":
    input_str = input("please input a list of numbers, split by space:").split()
    print("your input is:", input_str)
    numbers = [int(i) for i in input_str]
    input_list = input("please input a list of numbers, split by space:").split()
    print("your input is:", input_list)
    input_list = [int(i) for i in input_list]
    input_list = sort.quick_sort(input_list)
    print("after quick sort:", input_list[:numbers[1]])