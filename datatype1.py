
# data: dict = {'name': 'John', 'age': 30}

# Fundamental Datatypes
# 1. Numbers:

# Integers: Whole numbers without decimal points.
# Python
# x = 10  # Integer
# print(type(x))
# print(x)


# Floating-point numbers: Numbers with decimal points.
# Python
# y = 3.14  # Floating-point number
# y[0] = 1
# print(y)


# Complex numbers: Numbers with a real and imaginary part.
# Python
# j = 6
# z = 2 + 3 * j  # Complex number
# print(z)


# 2. Strings:

# Sequences of characters enclosed in quotes.
# Python
# name = "Alice"  # String
# print(name)


# 3. Boolean:

# Represents True or False values.
# Python
# is_student = True  # Boolean
# print(is_student)
# print(type(is_student))


# Sequence Datatypes
# 1. Lists:

# Ordered collections of elements, mutable.
# Python
# fruits = ["apple", "banana", "orange"]  # List #list index always starts with 0
# print(fruits)
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print("len of fruits", len(fruits))
# fruits[0] = "Watermelon"
# fruits.append("grapes")
# print(fruits)


# 2. Tuples:

# Ordered collections of elements, immutable.
# Python
# coordinates = (2, 5)  # Tuple
# coordinates[0] = 1
# print(coordinates)


# 3. Sets:

# Unordered collections of unique elements.
# Python
# vowels = {"a", "e", "i", "o", "u"}  # Set
# print(vowels)


# Mapping Datatype
# 1. Dictionaries:

# Unordered collections of key-value pairs. {"key":"value"}
# Python
# person = {"name": "Bob", "age": 30}  # Dictionary
# print(person)
# person["age"] = "60"
# print(person)


# Special Datatypes
# 1. NoneType:

# Represents the absence of a value.
# Python
# result = None  # NoneType

# def divide(a, b):
#     if b == 0:
#         return None
#     return a / b

# result = divide(10, 2)
# print(result)  # Output: 5.0

# result = divide(10, 0)
# print(result)  # Output: None
# print(type(result))


# 2. Bytes and Bytearray:

# Used to represent raw binary data.
# Python
# data = b"hello"  # Bytes
# # data[0] = b"I"
# # print(data[0])

# data_array = bytearray(data)
# print(data_array[0])
# data_array[0] = ord("Y")
# print(data_array[0])


# Mutability and Immutability
# Mutable: Values can be changed after creation (e.g., lists, dictionaries).
# Immutable: Values cannot be changed after creation (e.g., numbers, strings, tuples).

# Type Conversion
# Explicit conversion: Using built-in functions like int(), float(), str(), etc.
# Python
# x = 10
# y = float(x)  # Convert integer to float
# print(y)  # Output: 10.0


# Implicit conversion: Python automatically converts types in certain situations.
# Example
# Python
# # Create variables of different datatypes
# num = 10
# name = "Python"
# is_true = True
# fruits = ["apple", "banana"]
# coordinates = (2, 5)
# person = {"name": "Alice", "age": 30}

# # Perform operations on datatypes
# print(num + 5)
# print(name * 3)
# print(is_true and False)
# fruits.append("orange")
# print(fruits)
# print(person["name"])

# Type conversion
# x = 3.14
# y = int(x)
# print(y)


# Remember:

# Choose the appropriate datatype based on the nature of your data and the operations you need to perform.
# Be mindful of mutability and immutability when working with sequences and dictionaries.
# Use type conversion judiciously to avoid unexpected behavior.

a= 1_0000_00
b= 5_00_0

print(a*b)








