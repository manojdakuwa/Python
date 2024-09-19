# a = 5
# b = 5
# print("output for '==' for integer", a == b)  # Output: True
# print("output for 'is' for integer", a is b)  # Output: True

# x = [1, 2, 3]
# y = [1, 2, 3]
# print("output for '==' for List", x == y)  # Output: True #comparison operator check value 
# print("output for 'is' for List", x is y)  # Output: False #identity operator check memory object allocation

# g = x
# print( "output after copying object", x is g ) 

# Explanation:

# a == b: This expression compares the values of a and b. Since both a and b are integers with the value 5, they are considered equal, so the output is True.
# a is b: This expression compares the object identities of a and b. For small integer values like 5, Python often reuses the same object to optimize memory usage. Therefore, a and b are actually referencing the same object, so the output is True.
# x == y: This expression compares the values of the lists x and y. Since both lists contain the same elements in the same order, they are considered equal, so the output is True.
# x is y: This expression compares the object identities of x and y. In this case, x and y are two separate list objects, even though they have the same elements. Therefore, they are not the same object, so the output is False.
# Real-World Examples:

# Comparing ages: If you have two variables, age1 and age2, both containing the value 25, age1 == age2 will be True because they have the same value. However, age1 is age2 will be True only if they refer to the same object in memory (which is often the case for small integers).
# Comparing cars: If you have two variables, car1 and car2, both representing cars with the same make, model, and year, car1 == car2 will be True if they have the same attributes. However, car1 is car2 will be False unless they are the same exact car object (e.g., if you copied one car object to another).
# Key Points:

# The == operator compares values, while the is operator compares object identities.
# For small integer values, Python often reuses the same object to optimize memory usage.
# For mutable data types like lists, creating two separate objects with the same elements will result in different object identities.


a = 2 
b = 3
c = "3"
# d = a+b+c
# print(d)
# print(d)

# Here's the breakdown of what happens in each line:

# print(a+b+c):

# a + b evaluates to 5 (2 + 3).
# 5 + c is a concatenation operation because c is a string. It concatenates the integer 5 with the string "3" to produce the string "53".
# print(c+a+b):

# c + a is a concatenation operation, resulting in the string "32".
# "32" + b is another concatenation operation, resulting in the string "323".
# print(+c+a+b):

# The unary + operator has no effect on strings. It simply returns the original string.
# Therefore, +c is equivalent to c, and the expression becomes c + a + b, which is the same as the previous line.


a = [1, "2", 3]
b = [2, 4, "7"]
print(a[1] + b[1])
print(b[2] + a[2])