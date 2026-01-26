# def add_arguments():
#     total = 0
#     for num in args:
#         total += num
#     return total

# print(add_arguments(235, 25, 12, 3, 45, 13))

# keyword argument
# print("Dachi", "Giorgi", "Zurabi", sep=' ||| ')
#      0          1          2      sep


# packing
# vegetables = ("Pumpkin", "Cabbage", "Beetroot")

# product1, *rest = vegetables

# print(rest)

# *args - arguments
# **kwargs - keyword argument

# def greeting(visitor, *guests, special, **others):
#     print("Welcome " + visitor)
#     print("HOORAY " + special)
#     for guest in guests:
#         print("Howdy " + guest) 
    
#     for key in others:
#         print(f"Hello {key} {others[key]}")
# greeting("Irakli", "Luka", "Zurabi", "Dachi", "Giorgi", special="Nika", celebrity="Zaza", influencer="Dato")

# scope - წვდომის ხედვის არეალი
# lexial scope - გულსხმიობს ნებსმიერი ობიექტის ხელმისაწვდომობა კონკრეტულ კოდის ბლოკში და მის ქვევით


# def foramt_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return "Sum: " + str(result)
#     return wrapper

# @foramt_decorator
# def add_nums(x, y):
#     return x + y


# print(add_nums(2, 3))