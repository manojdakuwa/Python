# 1. Simple If-Else:

# If it's raining, take an umbrella.
# Else, go outside.


# 1. If-Else with Condition:

# If you are 18 or older, you can vote.
# Else, you cannot vote.


# 1. Nested If-Else:

# If you have money,
#   If you have time,
#     Go shopping.
#   Else,
#     Stay home.
# Else,
#   Look for a job.



# Python If-Else Examples with Various Data Types


# Numbers (Integers and Floats)



x = 11
if x > 10:
    print("x is greater than 10")
else:
    print("x is less than or equal to 10")



#Strings



name = "John"
if name == "John":
    print("Hello, John!")
else:
    print("Hello, unknown!")



#Boolean



isAdmin = True
if isAdmin:
    print("You are an admin.")
else:
    print("You are not an admin.")



#Lists



fruits = ["apple", "banana", "cherry"]
if "cake" in fruits:
    print("Apple is in the list.")
else:
    print("Apple is not in the list.")



#Tuples



colors = ("red", "green", "blue")
if "green" in colors:
    print("Green is in the tuple.")
else:
    print("Green is not in the tuple.")



#Dictionaries



person = {"name": "John", "age": 30}
if "name" in person:
    print("Name is", person["name"])
else:
    print("Name not found.")



#Sets



numbers = {1, 2, 3, 4, 5}
if 3 in numbers:
    print("3 is in the set.")
else:
    print("3 is not in the set.")



#Additional Python If-Else Features


#1. elif (else if):

x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


#1. in operator:

fruits = ["apple", "banana", "cherry"]
if "apple" in fruits:
    print("Apple is in the list.")


#1. is operator:

x = None
if x is None:
    print("x is None")


#1. Ternary operator:

x = 5
result = "x is greater than 10" if x > 10 else "x is less than or equal to 10"
print(result)
#

# Example 1: Simple Nested If-Else



x = 10
y = 20

if x > 5:
    if y > 15:
        print("Both conditions met")
    else:
        print("Only x > 5")
else:
    print("Neither condition met")



# Example 2: Real-World Scenario



age = 25
income = 50000
credit_score = 700

if age >= 21:
    if income >= 40000:
        if credit_score >= 650:
            print("Eligible for loan")
        else:
            print("Low credit score")
    else:
        print("Low income")
else:
    print("Underage")



# Example 3: Nested If-Else with Multiple Conditions



grade = 85
attendance = 90
participation = 95

if grade >= 80:
    if attendance >= 85 and participation >= 90:
        print("Excellent student")
    elif attendance >= 80 or participation >= 90:
        print("Good student")
    else:
        print("Needs improvement")
else:
    print("Failing grade")



# Example 4: Nested If-Else with Logical Operators



x = 5
y = 3
z = 2

if x > 4 and y > 2:
    if z == 2 or y > 4:
        print("Complex condition met")
    else:
        print("Simple condition met")
else:
    print("Neither condition met")



# Visual Representation


# To better understand nested if-else statements, consider the following visual representation:



# if (condition1):
#     if (condition2):
#         if (condition3):
#             # code block
#         else:
#             # code block
#     else:
#         # code block
# else:
#     # code block