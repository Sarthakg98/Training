# basic class definition in Python
# class Student:
#     name="John Doe"
#     age=20
    
# s1=Student()   
# print(s1.name)
# print(s1.age)

# init function in Python
# class Student:
#     def __init__(self, name, age):
#         self.name= name
#         self.age= age
        
#     def display(self):
#         print(f"Name: {self.name}, Age:{self.age}")
        
# s1=Student("John Doe", 20)
# s1.display()

# class Addition:
#     @staticmethod
#     def add(x,y):
#         return x + y
# s1 = Addition()
# print(s1.add(5,3))    
    
# create account class with 2 attributes- balance & account no and create methods for debit
# and credit operations. Create an object of the class and perform

# class Account:
#     def __init__(self, account_no, balance=0):
#         self.account_no = account_no
#         self.balance = balance
        
#     def credit(self, amount):
#         self.balance+= amount
#         print(f"Credited {amount}. New balance: {self.balance}")
    
#     def debit(self, amount):
#         if amount > self.balance:
#             print("Insufficient balance")
#         else:
#             self.balance -=amount
#             print(f"debited {amount}. New balance: {self.balance}")
            
# ac= Account("123456789", 1000)
# ac.credit(500)
# ac.debit(300)
# ac.debit(1500)  # This should show insufficient balance
#------------------------------------------------------------------------------------------------------------            
            
# private specifier in Python
# class Account:
#     def __init__(self, account_no, accpass):
#         self.account_no =account_no
#         self.__accpass= accpass

# acc1= Account("12345", "abcde")
# print(acc1.account_no)
# print(acc1.__acc_pass)  # This will raise an AttributeError because __acc_pass is private        

# ------------------------------------------------------------

# inheritance in Python

# class Animal:
#     def __init__(self, name):
#         self.name= name
        
# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} says woof!")
        
# class cat(Animal):
#     def meow(self):
#         print(f"{self.name} says meow!")
        
# # Creating instances of Dog and Cat
# dog =Dog("BUddy")
# cat = cat("whiskers")
# dog.bark()  # Output: Buddy says woof!
# cat.meow()  # Output: Whiskers says meow!
#------------------------------------------------------------------------------------------------------------                          

# class method in Python
# class Student:
#     school_name = "ABC School"  # class variable

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     # Instance method: uses self
#     def show(self):
#         print(f"Instance method: {self.name}, {self.age}, {self.school_name}")
            
#      #cls method using self   
#     @classmethod  
#     def change_school(cls, new_name):
#         cls.school_name = new_name
#         print(f"school name changed to {cls.school_name}")
     
#      # static method: uses neither self nor cls   
#     @staticmethod
#     def is_adult(age):
#         return age>=18
    
# # Creating an instance of Student
# s1 = Student("John Doe", 20)

# # Instance method
# s1.show()  # John Doe, 20, ABC School

# # Class method (can be called from instance or class)
# Student.change_school("XYZ School")  # Changes class variable
# s1.show()  # Now school is XYZ School

# # Static method
# print("Is adult?", Student.is_adult(20)) #True
# print("Is adult?", Student.is_adult(16)) #False

# ------------------------------------------------------------------------------------------------------------

#Method Resolution Order (MRO) in Python
# MRO IS A way Python determines the order in which 
# classes are looked up when searching for a method or attribute.
# It is particularly important in multiple inheritance scenarios.

# class A:
#     def func(self):
#         print("A's func")
        
# class B():
#     def func(self):
#         print("B's func") 
        
# class C(A,B):
#     def func(self):
#         print("C's Func")
        
# obj = C()   
# obj.func() # Output: C's Func

# ---------------------------------------------------------------------
 #map function in Python
# The map() function applies a given function to all items in an iterable (like a list or tuple) and returns a map object (which is an iterator).
# It is often used to apply a transformation to each item in a collection.
 # Output: [1, 4, 9, 16, 25] 

# def square(x):
#     return x*x
# numbers=[1,2,3,4,5]
# sq_numbers= list(map(square, numbers))
# print(sq_numbers)

#fliter function in Python
# The filter() function constructs an iterator from elements of an iterable for which a function returns true
# It is often used to filter out unwanted items from a collection.

# def greater_than_2(y):
#     return y>2
# numbers =[1,2,3,4,5,6]
# greater_th_2 = list(filter(greater_than_2, numbers))
# print(greater_th_2)   

# reduce function in Python
# The reduce() function from the functools module applies a 
# rolling computation to sequential pairs of 
# values in an iterable.

# from functools import reduce

# def sum_num(a,b):
#     return a+b

# numbers = [1,2,3,4,5,6]
# re = reduce(sum_num, numbers)
# print(re)

# --------------------------------------------------------------
#context manager in Python
# A context manager is a Python object that defines the runtime context to be established when executing a with statement.
# It is used to allocate and release resources precisely when you want to.
# The most common use case is file handling, where you want to ensure that a file is properly closed after its suite finishes, even if an exception is raised.
# A context manager is typically implemented using the contextlib.contextmanager decorator or by defining a class

# from contextlib import contextmanager

# @contextmanager
# def my_context():
#     print("Start")
#     yield "In the context"
#     print("End")

# # Use it
# with my_context() as val:
#     print(val)
    

# Output:
# Start
# In the context
# End   

# This code defines a context manager using the @contextmanager decorator.
# When the context is entered, it prints "Start", yields a value, and when the context is exited, it prints "End".
# The `with` statement is used to manage the context, ensuring that the setup and teardown code is executed properly.
# This is useful for managing resources like files, network connections, or database transactions, ensuring they are cleaned up after use.
# The context manager can be used to handle exceptions, manage resources, or perform setup and teardown operations in a clean and readable way.
# ----------------------------------------------------------------------

#threading in python
# Threading is a way to run multiple threads (smaller units of a process) concurrently
# in a single process. It allows for parallel execution of code, which can improve performance,
# especially in I/O-bound tasks or when you want to perform multiple operations simultaneously. 

# import threading
# import time

# def print_numbers():
#     for i in range(1,6):
#         print(f"Number: {i}")
#         time.sleep(1)
        
# def print_letters():
#     for letter in ['a', 'b', 'c', 'd', 'e']:
#         print(f"Letter: {letter}")
#         time.sleep(1)
        
# # Create threads
# t1 =threading.Thread(target=print_numbers)
# t2 =threading.Thread(target=print_letters)

# # Start threads
# t1.start()
# t2.start()

# # wait for both threads to finish
# t1.join()
# t2.join()  


# from multiprocessing import Process
# import time

# def count_down():
#     for i in range(5, 0, -1):
#         print(f"Countdown: {i}")
#         time.sleep(1)

# def count_up():
#     for i in range(1, 6):
#         print(f"Countup: {i}")
#         time.sleep(1)

# if __name__ == "__main__":
#     p1 = Process(target=count_down)
#     p2 = Process(target=count_up)

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print("✅ Done with multiprocessing!")

class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

s = Student("Alice")
print(s.get_name())

     
    
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

s = Student("Alice")
print(s.name)
            


    
       
        
        
        
                