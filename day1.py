# # Data Types
# integer_var = 10
# float_var = 3.14
# string_var = "Hello"
# boolean_var = True
# list_var = [1, 2, 3, 4, 5]
# tuple_var = (6, 7, 8)
# dictionary_var = {"a": 1, "b": 2}
# set_var = {9, 10, 11}

# print(f"Integer: {integer_var}, Type: {type(integer_var)}")
# print(f"Float: {float_var}, Type: {type(float_var)}")
# print(f"String: {string_var}, Type: {type(string_var)}")
# print(f"Boolean: {boolean_var}, Type: {type(boolean_var)}")
# print(f"List: {list_var}, Type: {type(list_var)}")
# print(f"Tuple: {tuple_var}, Type: {type(tuple_var)}")
# print(f"Dictionary: {dictionary_var}, Type: {type(dictionary_var)}")
# print(f"Set: {set_var}, Type: {type(set_var)}")

# print("\n--- Slicing Examples ---")
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(f"Original list: {my_list}")
# print(f"First three elements: {my_list[0:3]}")
# print(f"Elements from index 5 onwards: {my_list[5:]}")
# print(f"Last three elements: {my_list[-3:]}")
# print(f"Every second element: {my_list[::2]}")
# print(f"Reversed list: {my_list[::-1]}")

# my_string = "Python Slicing"
# print(f"Original string: {my_string}")
# print(f"Substring: {my_string[7:]}")

# print("\n--- Comprehension Examples ---")
# # List comprehension
# squares = [x**2 for x in range(10)]
# print(f"Squares (list comprehension): {squares}")

# # List comprehension with condition
# even_numbers = [x for x in range(20) if x % 2 == 0]
# print(f"Even numbers (list comprehension): {even_numbers}")

# # Dictionary comprehension
# square_dict = {x: x**2 for x in range(5)}
# print(f"Square dictionary (dict comprehension): {square_dict}")

# # Set comprehension
# unique_letters = {letter for letter in "Mississippi"}
# print(f"Unique letters (set comprehension): {unique_letters}")


#--------------------------------------------------------------------------------------------------------------------




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


# #generator in python
# def my_generators():
#     print("generator: before yield")
#     yield 1
#     print("generator: after yield")
#     yield 2
#     print("generator: after second yield")
#     yield 3

# my_gen = my_generators()

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


# Iterators and Generators

# --- Iterators --------------------------------------------------------------------------------------------------

# An iterator is an object that implements the iterator protocol, which consists of the methods __iter__() and __next__().
# The __iter__() method returns the iterator object itself, and the __next__() method returns the next item from the sequence.
# When there are no more items, __next__() raises the StopIteration exception.

# # Example of an iterator
# my_list = [1, 2, 3, 4]
# my_iterator = iter(my_list)

# print("--- Iterator Example ---")
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# # The next line would raise StopIteration:
# # print(next(my_iterator))

# # You can also iterate using a for loop (which implicitly uses the iterator protocol)
# print("\n--- Iterating with a for loop ---")
# for item in my_list:
#   print(item)

# # --- Generators ------------------------------------------------------------------------------------------------

# # Generators are a simple and powerful tool for creating iterators.
# # They are written like regular functions but use the `yield` statement instead of `return`.
# # When a generator function is called, it returns an iterator.
# # The `yield` statement pauses the function's execution and saves its state, resuming from where it left off on the next call to `next()`.

# # Example of a generator function
# def my_generator():
#   print("First item")
#   yield 1
#   print("Second item")
#   yield 2
#   print("Third item")
#   yield 3

# print("\n--- Generator Example ---")
# my_gen = my_generator()

# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# # The next line would raise StopIteration:
# # print(next(my_gen))

# # Generators are often used for creating infinite sequences or processing large datasets efficiently,
# # as they generate items on the fly and don't store the entire sequence in memory.

# # Example of an infinite generator
# def infinite_sequence():
#   num = 0
#   while True:
#     yield num
#     num += 1

# print("\n--- Infinite Generator Example (first 5 numbers) ---")
# gen = infinite_sequence()
# for _ in range(5):
#   print(next(gen))

# # Generator expressions (similar to list comprehensions but create generators)
# my_generator_expression = (x**2 for x in range(5))

# print("\n--- Generator Expression Example ---")
# print(next(my_generator_expression))
# print(next(my_generator_expression))
# print(next(my_generator_expression))
# print(next(my_generator_expression))
# print(next(my_generator_expression))
# # The next line would raise StopIteration:
# # print(next(my_generator_expression))

#------------------------------------------------------------------------------------------------------------
# Multithreading in Python

# Multithreading is a technique that allows a program to run multiple tasks concurrently within a single process.
# These tasks are called threads. Threads share the same memory space, which can make communication between them easier
# but also introduces challenges like race conditions and the need for synchronization.

# Python's `threading` module provides support for creating and managing threads.

# import threading
# import time

# # --- Creating Threads ---

# # You can create a thread by instantiating the `threading.Thread` class and passing a target function and its arguments.

# def my_thread_function(name):
#   """Function that runs in a separate thread."""
#   print(f"Thread {name}: starting")
#   time.sleep(2) # Simulate doing some work
#   print(f"Thread {name}: finishing")

# print("--- Thread Creation Example ---")

# # Create two threads
# thread1 = threading.Thread(target=my_thread_function, args=("Thread-1",))
# thread2 = threading.Thread(target=my_thread_function, args=("Thread-2",))

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for the threads to complete
# thread1.join()
# thread2.join()

# print("Main thread: all threads finished.")



# Python’s memory management (especially reference counting) is not thread-safe, 
# so the GIL prevents multiple threads from corrupting memory by only allowing one active thread at a time.

# import threading
# import time

# def count():
#     for i in range(10000000):
#         pass

# start = time.time()

# # Create two threads running the same function
# t1 = threading.Thread(target=count)
# t2 = threading.Thread(target=count)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end = time.time()
# print(f"Time taken with threads: {end - start:.2f} seconds")

#------------------------------------------------------------------------------------------------------------

# # Static Methods in Python

# @staticmethod is a decorator in Python.

# It defines a method inside a class that:

# Does NOT use self (the instance)

# Does NOT use cls (the class itself)

# class MathUtils:
    
#     @staticmethod
#     def add(x, y):
#         return x + y

# # You can call it without creating an object
# result = MathUtils.add(5, 3)
# print(f"Result: {result}")


