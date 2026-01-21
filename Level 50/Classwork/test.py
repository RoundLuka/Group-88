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


# მაღალი იერაქციის ფუნქციები: map, filter
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

# iterable
# nums = [2, 4, 6, 8, 10, 12]

# def four_multiple(x):
#     return x % 4 == 0

# filtered = filter(four_multiple, nums)
# print(list(filtered))

# def operation(x):
#     return x + 5


# result = map(operation, nums)

# print(list(result))

# products = {
#     "Apple": [12, 5, '2027-JAN-15'],
#     "Grapes": [15, 3, '2027-DEC-15'],
#     "Peach": [25, 2, '2030-JUN-13'],
#     "Berry": [21, 25, '2029-NOV-15'],
#     "Potato": [54, 14, '2028-AUG-12'],
#     "Tomato": [24, 7, '2027-FEB-15'],
#     "Pumpkin": [2, 15, '2027-OCT-15'],
# }

# new_products = filter(lambda key: products[key][0] > 20, products)
# print(list(new_products))


# nums = [2, 4, 6, 8, 10, 12]

# tripled = list(map(lambda x: x * 3, [2, 4, 6, 8, 10, 12]))
# print(tripled)

# data = [("B", 22, 1,), ("A", 12, 3), ("C", 14, 2) ]

# print(sorted(data, key=lambda x: x[1]))

# def total(price, count):
#     return price * count

# print(total(2,3))

# def greet():
#     return '123'

# print( greet )

# any = lambda name: "#" + name
# print(type(any))


# callback - ისეთი ფუნქცია რომელსაც სხვა ფუნქციას გადავცემ პარამეტრად და სხვანგან გამოვიძახებ
# def x():
#     return 1


# def eveulate(func):
#     return func()

# eveulate(x)


# exam_scores = [85, 62, 95]

# def is_passing(score):
#     return score >= 70

# status = list(map(is_passing, exam_scores))
# print(status)


# decorator

def decorator(func):
    def wrapper():
        print("-----Start------")
        func()
        print("-----End------")
    return wrapper

@decorator
def func1():
    print("Hello function 1")
    return '5'

# ------------

@decorator
def func2():
    print("fujnction 2")

func1()
func2()