

# f = 'manoj'
# k = 'xyx'
# y =123
# a = 0.25

# # # #object value in quotes = string
# # # #object value without qoutes and without decimal = integer
# # # #object value without quotes and with decimal = float
# # # #object value with true or false is called Boolean
# # # #datatype = is nothing but define type of your object
# a = "mannsetech" 
# b = 123 
# c = 0.23
# d = True
# e = False 

# a += " with Manoj"
# print(a)
# b = "xyz"
# print(b)



#print(type(a)) #to know the type of data type

# # a = "manoj" #this object is created in memory with name 'a' 
# # a += " dakuwa" #concatenate 

# # #immutable - 
# # # First 'a; which is cfreated in memory is being garbage collected

# # a = "manoj"
# # a +="dakuwa"
# # print(a)

# # a10 ="manoj"
# # _a = "santosh"

# #python is case sensitive

# # a10 = 10
# #a10 is different then A10

# # q= "abc"

# #types of varoiable :
# # a = "abc" #string
# # b ="xyz" #string
# # c = 123 #integer
# # d = 0.245 #float
# # e = True 

# # x = 10
# # # print("x :", x)
# # x =20
# # print("x ", x)


# a, b, c = 1, 2, 3 #multiple assignment

# print(a)
# print(b)
# print(c)


# # x =10
# # y = 15
# # print(" 1. x + y =", x+y) 

# # def greet(): #function = we have to start writing fucntion with def keyword
# #     print("2. x + y =", x+y)

# # greet()

# #REPL #interview for begginer #https://realpython.com/python-repl/
# # go to command prompts
# # type python press enter
# # type print("hello world") press enter


# #global variable


# def greet(): #a parameter
#     print("a =", a) #a is local variable
#     #inside this function whatever var is created is global for this fucntion
#     stud = "Student"
#     print("a :", a)
#     print("b :", stud)
#     return stud

# a = "mannsetech"  #global variable
# # b = greet(a)
# # c= greet("Student")
# stud = greet()
# print("stud :", stud) 
# print("c :", c) 

# # print("# b ", b)
# # print("with concatenate b :" + b)
# # print(f"with f string b :{b}")

# #in built function = print, any function that python provides is called built in
# #user defined i.e greet()


# Immutable Data Types:

# Immutable data types in Python are those whose values cannot be changed after they are created. Once assigned, their contents remain fixed throughout their lifetime. This means that any operations performed on them create new objects rather than modifying the existing ones.

# Memory Management:

# When you assign a new value to an immutable data type, Python does the following:

# Creates a new object: A new object is created in memory to store the new value.
# Assigns the new object: The reference to the old object is updated to point to the newly created object.
# Garbage collection: If there are no other references to the old object, Python's garbage collector will reclaim its memory for future use.
# Example:

# Python
# s = "hello" 
# s += " world"
# Use code with caution.

# In this example:

# Initially, the string "hello" is created in memory, and s refers to it. s = "hello" 
# When s += " world" is executed, a new string object "hello world" is created in memory. print(s) = "Hello World"
# The reference s is updated to point to the new string object.
# If there are no other references to the original "hello" string, it will be garbage-collected.
# Key Points:

# Immutable data types are not modified in-place.
# Assigning a new value to an immutable variable creates a new object.
# Python's garbage collector automatically reclaims memory for unused objects.
# Additional Considerations:

# While immutable data types can be more efficient in terms of memory management, excessive creation of new objects can still impact performance if not managed carefully.
# In some cases, using mutable data types might be more appropriate for performance reasons, especially when dealing with large datasets.
# By understanding how immutable data types work and how memory is managed in Python, you can write more efficient and effective code.

# # Mutable data types
# my_list = [1, 2, 3]
# my_list.append(4)  # Modifying the list
# print(my_list)

# my_dict = {"name": "Alice", "age": 30}
# my_dict["age"] = 31  # Modifying the dictionary

# # Immutable data types
# my_string = "Hello"
# my_string[0] = "M"  # This will raise an error

# my_tuple = (1, 2, 3)
# # my_tuple[0] = 4  # This will raise an error

# def greet():
#     x = "Mannsetech with Manoj"
#     print(x)

# greet()

# greet = "Hello World"
# print("# greet ", greet)
# print("with concatenate greet :" + greet)
# print(f"with f string greet :{greet}")







