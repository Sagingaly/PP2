# 1)from functools import reduce
#
# def multiply_list(numbers):
#     return reduce(lambda x, y: x*y, numbers)
#
#
# input_str = input("Enter a list of numbers separated by spaces: ")
# numbers = list(map(int, input_str.split()))
# result = multiply_list(numbers)
# print(result)

# 2)def count_upper_lower(string):
#     upper_count = sum(1 for c in string if c.isupper())
#     lower_count = sum(1 for c in string if c.islower())
#     return (upper_count, lower_count)
#
#
# string = str(input())
# upper_count, lower_count = count_upper_lower(string)
# print("Number of upper case letters:", upper_count)
# print("Number of lower case letters:", lower_count)

#4) def is_palindrome(string):
#     return string == ''.join(reversed(string))
#
#
# string1 = str(input())
# string2 = str(input())
# print(string1, "is a palindrome:", is_palindrome(string1))
# print(string2, "is a palindrome:", is_palindrome(string2))



# 4)import time
# import math
#
# def sqrt_after_milliseconds(number, milliseconds):
#     time.sleep(milliseconds/1000)
#     return math.sqrt(number)
#
# number = int(input())
# milliseconds = int(input())
# result = sqrt_after_milliseconds(number, milliseconds)
# print(f"Square root of {number} after {milliseconds} milliseconds is {result}")

# 5)def all_elements_true(my_tuple):
#     return all(my_tuple)
#
# t1 = input("Enter a comma-separated list of boolean values for t1: ")
# t2 = input("Enter a comma-separated list of boolean values for t2: ")
# t1 = tuple(map(str.strip, t1.split(',')))
# t2 = tuple(map(str.strip, t2.split(',')))
# t1 = tuple(map(lambda x: x.lower() == "true", t1))
# t2 = tuple(map(lambda x: x.lower() == "true", t2))
# print("All elements of t1 are true:", all_elements_true(t1))
# print("All elements of t2 are true:", all_elements_true(t2))
