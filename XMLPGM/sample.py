# class Company:
#     def __init__(self, company_name):
#         self.company_name = company_name

#     def company_info(self):
#         print(f"Company: {self.company_name}")

# class Employee(Company):
#     def __init__(self, company_name, employee_name, employee_id):
#         super().__init__(company_name)  
#         self.employee_name = employee_name
#         self.employee_id = employee_id

#     def employee_info(self):
#         super().company_info() 
#         print(f"Employee Name: {self.employee_name}")
#         print(f"Employee ID: {self.employee_id}")


# emp = Employee("TCS", "SHINU", "s/w-1234")
# emp.employee_info()


# class Book:
#     def __init__(self, title):
#         self.title = title

#     # def __hash__(self):
#     #     return hash(self.title)

#     def __eq__(self, other):
#         return isinstance(other, Book) and self.title == other.title

    

# book1 = Book("Python 101")
# book2 = Book("Python 101")

# print(hash(book1))  
# print(book1 == book2)  

# book_set = {book1,book2}
# for book in book_set:
#     print(book.title)
# print(book2 in book_set) 

# print(book1 == book2)
# print(book1 is book2)

# squre={x:x**2 for x in range(1,10)}
# print(squre)



# a=[1,2,3,4]
# b=[1,2,3,4]
# print(a == b)
# print(a is b)
    

# z={

# }
# print(type(z))


# s=set()
# print(type(s))

# tp=()
# print(type(tp))

# li=[]
# print(type(li))

# Sample code demonstrating the use of 'pass'

# def do_nothing():
#     pass  

# class EmptyClass:
#     pass  

# for i in range(5):
#     if i == 3:
#         pass  
#     else:
#         print(f"Processing number: {i}")
# .................................................................................................................

# def sample_function(*args, **kwargs):
#     print("Positional arguments (args):")
#     for arg in args:
#         print(f"  - {arg}")
    
#     print("\nKeyword arguments (kwargs):")
#     for key, value in kwargs.items():
#         print(f"  - {key}: {value}")

# # Call the function with *args and **kwargs
# sample_function(10, 20, 30,name="Alice", age=25, city="Paris" )

# ................................................................................................................
# from functools import reduce

# # Sample list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# squares = list(map(lambda x: x**2, numbers))
# print("Squares:", squares)

# evens = list(filter(lambda x: x % 2 == 0, numbers))
# print("Even numbers:", evens)


# sum_all = reduce(lambda x, y: x + y, numbers)
# print("Sum of all numbers:", sum_all)


# product_all = reduce(lambda x, y: x * y, numbers)
# print("Product of all numbers:", product_all)
# ...............................................................................................................


# Define a lambda to multiply two numbers
# multiply = lambda x, y: x * y
# result = multiply(6, 7)

# print("6 multiplied by 7 is:", result)


# ....................................
# List of tuples (name, age)
# people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

# # Sort by age using lambda
# sorted_people = sorted(people, key=lambda person: person[1])

# print("Sorted by age:", sorted_people)


# a=10
# b=20
# if a > b:
#     pass
# else:
#     print("a is not greater than b, so we do nothing here.")

# def sample_function(*args,**kwargs):
#     print("positinal arguments")
#     for x in args:
#         print(x)

#     print("keyword arguments:")
#     for key,value in kwargs.items():
#         print(f"{key} :{value}")

# sample_function(10,20,30,55,name="shinu",age=25,city="tdpa")


# res=lambda x,y:x+y
# print(res(1,3))

# number=(1,2,3,4,5,6,7)
# res=list(map(lambda x:x**2,number))
# print(res)


# number=[1,2,3,4,5,6,7]
# res=list(filter(lambda x:x%2==0,number))
# print(res)

# import functools 
# number=[1,2,3,4,5,6]
# res=functools.reduce(lambda x,y:x+y,number)
# print(res)

# with open("D:\jThread\demo.txt","r")as file:
#     result=file.read()
#     print(result)


    
# with open("D:\jThread\demo.txt","a")as file:
#     file.write("sample class\n")

# with open("D:\jThread\demo.txt","w")as file:
#     file.write("sample class\n")

# try:
#  with open("F:\\jthread\\integer.txt", "r") as file:
#     numlist = file.readlines()
#     sum = 0
#  for i in numlist:
#     sum = sum + int(i)
#     print("The sum of the number",sum)
# except FileNotFoundError:
#     print("File not found....")
# finally:
#     file.close()


# def sample_program():
#     for i in range(1,10):
#         yield i

# for number in sample_program():
#     print(number)

# def mydec(func):
#     def wrapper():
#         print("befor execution")
#         func()
#         print("after execution")
#     return wrapper


# @mydec
# def sample_function():
#     print("hello..")

# # Define a 1-level nested list
# nested = [[1, 2], [3, 4], [5, 6]]

# # Use list comprehension to flatten it
# flat = [item for sublist in nested for item in sublist]

# # Print the flattened list
# print("Flattened list:", flat)








l1=['anu','vasu','midhu']#anu vasu
for i in l1:
    
    if "a" in i:
        print(i)
