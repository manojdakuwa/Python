# A `for` loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any other iterable object. Each element in the sequence is accessed one by one in the loop. Here's a basic syntax for a `for` loop in Python:

# ```python
# for item in iterable:
#     # code to execute for each item
# ```

# ### Examples of Using `for` Loop with Different Data Types:

# 1. **List:**
fruits = ['apple', 'banana', 'cherry', "MannSetech"]

# for val in fruits:
#     print(val)
    # ret = False
    # if fruit == "apple":
    #     ret = True
    #     print(ret)


# 2. Tuple:

# numbers = (1, 2, 3, 4, 5)
# for number in numbers:
#     print(number)



# 3. Dictionary:


# person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
# for key in person:
#     print(key, person[key])


# 4. Set:
   
# colors = {'red', 'green', 'blue'}
# for color in colors:
#     print(color)



# 5. String:

# word = "hello"
# for letter in word:
#     print(letter)






# ### Using `for` Loop with `range()` Function:

# The `range()` function generates a sequence of numbers, which is often used to specify the number of times a loop should iterate.


# for i in range(5):  # generates numbers 0 to 4
#     print(i)



# ### Iterating with Index Using `enumerate()`:

# If you need the index while iterating over a sequence, you can use the `enumerate()` function.


# animals = ['cat', 'dog', 'rabbit'] ---> 
# # print(animals[1])
# for index, animal in enumerate(animals):
#     print(index, animal)


# ### Nested `for` Loops:

# You can also use nested `for` loops to iterate over nested structures, like a list of lists.


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for row in matrix:
#     # print(row)
#     for element in row:
#         # print(element)
#         print(element, end=' ')
#     print()  # for new line after each row



# These are the basic ways to use `for` loops in Python with different data types. 



# ...............................................


# ### 2. Using `for` Loop Backward

# To iterate over a sequence in reverse order, you can use the `reversed()` function or manipulate the `range` function.

# Using `reversed()` with a List:

# fruits = ["apple", "banana", "cherry"] #<----
# for fruit in reversed(fruits):
#     print(fruit)


# Using `range()` to Iterate Backward:

# for i in range(5, 0, -1):  # Will iterate from 5 to 1
#     print(i)


# Iterating Over a String in Reverse:


# word = "hello"
# for letter in reversed(word):
#     print(letter)

# word = "hello"
# print("checking slice : ", word[0:2])

# Alternatively, you can use slicing to reverse the sequence:

# Using Slicing with a List:


# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits[::-1]:
#     print(fruit)


# Using Slicing with a String:


# word = "hello"
# for letter in word[::-1]
#     print(letter)

# These examples should give you a good understanding of how to use `for` loops in Python to iterate over different data types and how to iterate backward.