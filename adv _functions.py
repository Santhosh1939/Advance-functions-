# Coding exercises:
# Write a Python function square_all(numbers) that takes a list of numbers as
# input and returns a new list containing the square of each number in the
# input list. Use the map() function with a lambda function to implement this.

# def square_all(numbers):
#     return list(map(lambda x: x ** 2, numbers))
# squared_numbers = square_all([1, 2, 3, 4, 5])
# print(squared_numbers)


# Write a Python function filter_positive(numbers) that takes a list of numbers
# as input and returns a new list containing only the positive numbers from
# the input list. Use the filter() function with a lambda function to implement this.StopAsyncIteration

# def filter_positive(numbers):
#     return list(filter(lambda x: x > 0, numbers))
# input_numbers = [-10, -5, 0, 5, 10]
# positive_numbers = filter_positive(input_numbers)
# print(positive_numbers) 




# Write a Python function calculate_factorial(n) that calculates the factorial of
# a given number n . Use the reduce() function with an appropriate lambda
# function to implement this.


# from functools import reduce
# n=int(input("enter a number : "))
# def calculate_factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return reduce(lambda x, y: x * y, range(1, n + 1))

# factorial = calculate_factorial(n)
# print(factorial)  



# Write a Python function count_vowels(string) that takes a string as input and
# returns the count of vowels (a, e, i, o, u) in the input string. Use the reduce()
# function with an appropriate lambda function to implement this.

# from functools import reduce

# def count_vowels(string):
#     vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     return reduce(lambda count, char: count + (1 if char in vowels else 0), string, 0)

# input_string = "Hello santhosh, how are you?"
# vowel_count = count_vowels(input_string)
# print(vowel_count) 
#  # Output: 9



