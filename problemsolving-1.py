# # 1. Calculate area and perimeter of a rectangle
# def calculate_rectangle(length, width):
#     area = length * width
#     perimeter = 2 * (length + width)
#     return area, perimeter



# print(".........................................................................................")
# print(".........................................................................................")
# print(".........................................................................................")

# length = 5
# width = 3
# area = length * width
# perimeter = 2 * (length + width)
# print("Area:", area)
# print("Perimeter:", perimeter)

# print(".........................................................................................")
# print(".........................................................................................")
# print(".........................................................................................")

# 2. Check if a number is prime
#Range Datatype
# for i in range(2, 4, 1): #range datatype (start, stop, step) (2, 11(exclude), steps=2) 2, 3
#     print(i)

# def is_prime(num): #17
#     if num <= 1: #base condition
#         print("base conition")
#         return False
#     for i in range(2, int(num**0.5) + 1): #range(2, 17**0.5+1)  #5  #range(2, 6) 2, 3, 4, 5
#         print("for loop", int(num**0.5) + 1)
#         if num % i == 0: #31%2 ==0 => false, 31%3==0 =>false, 31%4==0 =>false, 31%5==0, 
#             print("num % i == 0 is checked")
#             return False
#     return True

# print(".........................................................................................")
# print(".........................................................................................")
# print(".........................................................................................")
# # 3. Find maximum and minimum values in a list
# def find_max_min(numbers): #find_max_min([10, 5, 20, 3, 8])
#     max_num = numbers[0] #10
#     min_num = numbers[0] #10
#     for num in numbers:
#         if num > max_num: #num =10 , max_num  = 10, [num = 5 max_num = 10 min_number=10]
#             max_num = num #[max_num = 20]
#         if num < min_num: #[]
#             min_num = num #[min_number = 3] # max_10, min=5
#         # print(num, max_num, min_num)
#     return max_num, min_num

# print(".........................................................................................")
# numbers = [10, 5, 20, 3, 8] #[[10, 5, 20, 3, 8, 50, 0, 1, -1]]

# maximum = max(numbers)
# minimum = min(numbers)

# print("Maximum value:", maximum)
# print("Minimum value:", minimum)
# print(".........................................................................................")
# print(".........................................................................................")
# # 4. Swap values of two variables without a temporary variable
def swap_values(x, y): #x =5, y= 6 => after swap x =6, y=5
    x = x + y #x = 10 + 20 = 30
    print("x", x)
    y = x - y #y = 10-20 ; y = 10
    
    print("y", y)
    x = x - y #x = 30 - 10 = 20 Q#bit operator use karke solve kijiye
    
    print("x", x)
    return x, y

# print(".........................................................................................")
a = 10
b = 20

a, b = b, a #tuple 

# print("a:", a)
# print("b:", b)
# print(".........................................................................................")
# print(".........................................................................................")
# # 5. Convert Celsius to Fahrenheit
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# print(".........................................................................................")
# print(".........................................................................................")
# print(".........................................................................................")
# Example usage
# length = 6
# width = 4
# area1, perimeter1 = calculate_rectangle(length, width)
# print("Area:", area1)
# print("Perimeter:", perimeter1)

# print(".........................................................................................")
# num = 31
# if is_prime(num):
#     print(num, "is a prime number.")
# else:
#     print(num, "is not a prime number.")

# print(".........................................................................................")
# numbers = [10, 5, 20, 3, 8]
# max_num, min_num = find_max_min(numbers)
# print("Maximum value:", max_num)
# print("Minimum value:", min_num)

# print(".........................................................................................")
# x = 10
# y = 20
# x, y = swap_values(x, y)
# print("x =", x, "y =", y)

# print(".........................................................................................")
celsius = 30
fahrenheit = celsius_to_fahrenheit(celsius)
print(celsius, "Celsius is equal to", fahrenheit, "Fahrenheit.")