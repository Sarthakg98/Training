# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("decorator: before function call\n")
#         result = func(*args, **kwargs)
#         print("decorator: after function call \n")
#         return result
#     return wrapper
# @decorator
# def my_function(x, y):
#     print(f"my_function: {x}, {y} ")
#     return x + y
# if __name__ == "__main__":
#     result = my_function(5, 10)
#     print(f"Result: {result}")
# Output:
# decorator: before function call
# my_function: 5, 10
# decorator: after function call
# Result: 15
# This code defines a decorator that prints messages before and after the function call,
# and applies it to a simple function that adds two numbers.
# The decorator is applied using the @ syntax, which is a common Python idiom for decorators.
# The main block calls the decorated function and prints the result.
# The decorator pattern is a design pattern that allows behavior to be added to individual objects,
# either statically or dynamically, without affecting the behavior of other objects from the same class.
# This example demonstrates how to use a decorator to enhance the functionality of a function.
# The decorator can be used to log function calls, enforce access control, or modify input/output
# without changing the function's code. 


#generator in python
def my_generators():
    print("generator: before yield")
    yield 1
    print("generator: after yield")
    yield 2
    print("generator: after second yield")
    yield 3

my_gen = my_generators()

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

