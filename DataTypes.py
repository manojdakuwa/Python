# Introduction
# Overview of Datatypes in Python
# Datatypes in Python are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, Python data types are classes, and variables are instances (objects) of these classes.

# Importance of Datatypes
# Datatypes are essential in programming as they help to:

# Determine the type of data that can be stored in a variable
# Perform operations on the data
# Ensure data integrity and accuracy
# Improve code readability and maintainability
# Types of Datatypes in Python
# Python has several built-in datatypes, including:

# Numeric Datatypes: int, float, complex
# Sequence Datatypes: list, tuple, range
# Mapping Datatypes: dict
# Set Datatypes: set, frozenset
# Boolean Datatype: bool
# Binary Datatypes: bytes, bytearray, memoryview
# None Datatype: NoneType

# Numeric Datatypes
# Introduction to Numeric Datatypes
# Numeric datatypes in Python are used to represent numbers. They include integers, floating-point numbers, and complex numbers.

# Types of Numeric Datatypes
# Integers: int
# Represent whole numbers, either positive or negative
# Can be any size, limited only by available memory
# Floating-Point Numbers: float
# Represent decimal numbers, either positive or negative
# Have a limited number of decimal places (15-17)

# Complex Numbers: complex
# Represent numbers with real and imaginary parts
# Can be represented in the form a + bj, where a and b are real numbers
# Operations on Numeric Datatypes
# Numeric datatypes support various operations, including:

# Arithmetic operations: +, -, *, /, %
# Comparison operations: ==, !=, <, >, <=, >=
# Logical operations: and, or, not
# Sequence Datatypes
# Introduction to Sequence Datatypes
# Sequence datatypes in Python are used to represent ordered collections of data. They include lists, tuples, and ranges.

# Types of Sequence Datatypes
# Lists: list
# Represent ordered collections of data
# Can contain any type of data
# Dynamic size, can grow or shrink as elements are added or removed

# Tuples: tuple
# Represent ordered collections of data
# Can contain any type of data
# Static size, cannot grow or shrink

# Ranges: range
# Represent a sequence of numbers
# Can be used to generate a sequence of numbers
# Operations on Sequence Datatypes
# Sequence datatypes support various operations, including:

# Indexing and slicing: accessing individual elements or subsets of elements
# Iteration: looping over elements in the sequence
# Concatenation: combining two or more sequences
# Mapping Datatypes
# Introduction to Mapping Datatypes
# Mapping datatypes in Python are used to represent key-value pairs. They include dictionaries.

# Types of Mapping Datatypes
# Dictionaries: dict
# Represent key-value pairs
# Can contain any type of data
# Dynamic size, can grow or shrink as key-value pairs are added or removed
# Operations on Mapping Datatypes
# Mapping datatypes support various operations, including:

# Key-value pair operations: accessing and modifying individual key-value pairs
# Iteration: looping over key-value pairs in the dictionary

# Set Datatypes
# Introduction to Set Datatypes
# Set datatypes in Python are used to represent unordered collections of unique data. They include sets and frozensets.

# Types of Set Datatypes
# Sets: set
# Represent unordered collections of unique data
# Can contain any type of data
# Dynamic size, can grow or shrink as elements are added or removed
# Frozensets: frozenset
# Represent unordered collections of unique data
# Can contain any type of data
# Static size, cannot grow or shrink
# Operations on Set Datatypes
# Set datatypes support various operations, including:

# Union and intersection: combining two or more sets
# Difference and symmetric difference: finding the difference between two sets
# Membership testing: checking if an element is in a set
# Boolean Datatype
# Introduction to Boolean Datatype
# The Boolean datatype in Python is used to represent true or false values.

# Operations on Boolean Datatype
# The Boolean datatype supports various operations, including:

# Logical operations: and, or, not
# Binary Datatype
# Introduction to Binary Datatype
# Binary datatypes in Python are used to represent binary data. They include bytes, bytearray, and memoryview.

# Types of Binary Datatypes
# Bytes: bytes
# Represent binary data
# Can contain any type of binary data
# Static size, cannot grow or shrink
# Bytearray: bytearray
# Represent binary data
# Can contain any type of binary data
# Dynamic size, can grow or shrink as elements are added or removed
# Memoryview: memoryview
# Represent a view of binary data
# Can contain any type of binary data
# Dynamic size, can grow or shrink as elements are added or removed
# Operations on Binary Datatype
# Binary datatypes support various operations, including:

# Indexing and slicing: accessing individual elements or subsets of elements
# Iteration: looping over elements in the binary data
# Concatenation: combining two or more binary data
# Calling Variables from One File to Another File
# Importing Modules
# To call variables from one file to another file, you need to import the module that contains the variables.

# Example
# Suppose you have a file called data.py that contains the following variables:

# data = {'name': 'John', 'age': 30}
# To access the data variable from another file called main.py, you need to import the data module:

# import data
# You can then access the data variable as follows:

# print(data.data['name'])
# Importing Specific Variables
# You can also import specific variables from a module instead of importing the entire module:

# from data import data
# You can then access the data variable as follows:

# print(data['name'])
# Importing Variables with Aliases
# You can also import variables with aliases:

# from data import data as d
# You can then access the data variable as follows:

# print(d['name'])
# I hope this helps! Let me know if you have any questions or need further clarification.