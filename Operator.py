# Operators in Python are symbols or keywords used to perform operations on values or variables. 
# They allow you to manipulate data, perform calculations, make comparisons, and control the flow of your program.

# Types of operators:
# 1. Arithmetic
# 2. comparison
# 3. Logical Operators
# 4. Membership Operators
# 5. Identity Operators

# Arithmetic Operators:
# Addition (+): Adds two numbers.
# Python
# result = 5 + 3
# a =5 
# b= 3
# result = a+b
# print(result)  # Output: 8

# Subtraction (-): Subtracts one number from another.
# Python
# result = 10 - 4
# a = 10
# b= 4
# result = a-b
# print(result)  # Output: 6

# Multiplication (*): Multiplies two numbers.
# Python
# result = 3 * 7
# a = 3
# b= 7
# result = a * b
# print(result)  # Output: 21


# Division (/): Divides one number by another.
# Python
# result = 17 / 3
# print(result)  # Output: 5.0


# Floor Division (//): Divides two numbers and returns the integer quotient.
# Python
# result = 17 // 3
# print(result)  # Output: 5


# Modulo (%): Returns the remainder of the division.
# Python
# result = 17 % 3
# print(result)  # Output: 2


# Exponentiation (**): Raises a number to a power.
# Python
# result = 2 ** 3
# print(result)  # Output: 8


# Comparison Operators:

# Equal to (==): Checks if two values are equal.
# Python
# result = 5 == 5
# print(result)  # Output: True


# Not equal to (!=): Checks if two values are not equal.
# Python
# result = 5 != 3
# print(result)  # Output: True


# Greater than (>): Checks if the left operand is greater than the right operand.
# Python
# result = 7 > 3
# print(result)  # Output: True


# Less than (<): Checks if the left operand is less than the right operand.
# Python
# result = 2 < 5
# print(result)  # Output: True


# Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand.
# Python
# result = 5 >= 6
# print(result)  # Output: True


#   
# Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.
# Python
# result = 4 <= 7
# print(result)  # Output: True


# Logical Operators:

# And (and): Returns True if both operands are True.
# Python
# result = True and False
# print(result)  # Output: False


# Or (or): Returns True if at least one operand is True.
# Python
# result = True or False
# print(result)  # Output: True


# Not (not): Negates the boolean value of an operand.
# Python
# result = not True
# print(result)  # Output: False

# result1 = not False
# print(result1)  # Output: True


# Membership Operators:

# In (in): Checks if a value is present in a sequence.
# Python
# my_list = [1, 2, 3]
# result = 2 in my_list
# print(result)  # Output: True


# Not in (not in): Checks if a value is not present in a sequence.
# Python
# my_string = "hello"
# result = "z" not in my_string
# print(result)  # Output: True

# Identity Operators:

# Is (is): Checks if two objects are the same object in memory.
# Python
# x = "s"
# y = "s"
# result = x is y
# print(result)  # Output: True

# The output is True because in Python, for small integer values (typically in the range of -5 to 256), Python creates a pool of pre-existing objects to optimize memory usage.

# When you assign the value 5 to both x and y, Python doesn't create two separate integer objects. Instead, it looks for an existing integer object with the value 5 in its pool. Since both x and y are referring to the same pre-existing integer object, the is operator returns True.

# Key points to remember:

# Integer Pooling: Python's optimization technique of reusing integer objects within a specific range.
# Object Identity: The is operator compares the memory addresses of objects.
# Value Equality: The == operator compares the values of objects.
# Additional Considerations:

# While integer pooling is common for small integer values, it's not guaranteed for all data types or larger values.
# For floating-point numbers and other data types, Python typically creates new objects for each value.

# Is not (is not): Checks if two objects are not the same object in memory.
# Python
# x = [1, 2, 3]
# y = [1, 2, 3]
# result = x is not y
# print(result)  # Output: True

# Understanding Identity Operators in Python

# Identity operators in Python (is and is not) are used to compare the memory addresses of two objects. 
# In essence, they check if two variables are referring to the exact same object in memory.

# Key Points:

# Memory Address: Each object in Python has a unique memory address.
# Object Identity: Two objects are considered identical if they have the same memory address.
# Value Equality: While two objects might have the same value, they may not necessarily be the same object.

# When to Use Identity Operators:

# Comparing object references: When you want to check if two variables are pointing to the exact same object.
# Optimizing code: In certain scenarios, using is can be more efficient than comparing values, especially for immutable objects.
# Debugging: To identify unexpected behavior or memory leaks, you can use is to check if objects are being reused or if there are unintended references.

# Example 1: Same object
# x = 5
# y = x
# print(x is y)  # Output: True (x and y refer to the same integer object)


# # Example 2: Different objects, same value
# a = [1, 2, 3]
# b = [1, 2, 3]
# print(a is b)  # Output: False (a and b are different list objects, even though they have the same elements)

# # Example 3: Immutable objects with the same value
# c = "hello"
# d = "hello"
# print(c is d)  # Output: True (For immutable data types like strings, Python often reuses objects with the same value)