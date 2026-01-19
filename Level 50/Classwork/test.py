# def any(num1, num2):
#     return num1 + num2

# print(any(5))


# def welcome():
#     return 'Hello World'

# def goodbye():
#     return 'See you next time'

# def higher_func(func):
#     print(func())

# higher_func(welcome)
# higher_func(goodbye)

# def book_title(title):
#     return "Book title: " + title
# def info(title, func):
#     return book_title(title)

# print(info("The Great Gatsby", book_title))


# Higher Order Function - მაღალი იერარქიის ფუნქცია არის ისეთი ფუქნცია რომელიც სხვა ფუნქცია(ფუნქციებს) ღებულბოს პარამეტრად და (ან) აბრუნებსმ მათ
# 


# def greet():
#     print("Hello World")

# def welcome(user):
#     print("Welcome,", user)

# welcome("Irakli")
# welcome("Zurabi")

# lambda
# map, filter

# my_numbers = [11, 5, 7, 13, 4, 5]

# def double(x):
#     return x * 2

# print(list(map(double, my_numbers)))

# def square(num):
#     return num ** 2

# print(manual_map(square, [1, 2, 3, 4, 5, 6]))


# lambda - ფუნქცია



# def manual_map(func, arr):
#     result = []
#     for element in arr:
#         result.append(func(element))
#     return result
    

# def manual_fitler(func, iterable):
#     result = []
#     for element in iterable:
#         if func(element):
#             result.append(element)
#     return result

