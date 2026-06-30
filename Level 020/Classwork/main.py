# conditional statement

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))


# if num1 > num2: 
#     print("num1 is greater then num2")
# elif num1 < num2:
#     print("num2 is greater then num1")
# else:
#     print("The numbers are equal")

# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is positive")
# elif num < 0:
#     print("The number is negative")
# else:
#     print("Number is netural, zero (0)")


# for x in range(200):
#     print("Repeat")

# print("Stop")

# seats = 100
# while seats > 0:
#     print(seats)
#     seats = seats - 1

# List - სია, მონაცემთა ტიპი, რომელშიც შეგვიძლია რამდენიმე ელემენტის შენახავა, python-ში სიის შესაქმნელად ვიყენებთ [] კვადრატულ ბრჩხილებს

# users_balance = [2050, 1500, 1300, 600]

# print(type(["Luka", "Giorgi", "Irakli", "Bacho", "Nika", "Demetre"]))

# ყველა ელემენტს აქვს სიაში გარკვეული პოზიცია, ინდექსი

# my_data = [True, 2.7, "Luka", 15, True, "Luka"]
# # index:    0      1         2     3

# print(my_data[0])

# print(my_data[0])
# print(my_data[1])
# print(my_data[2])
# print(my_data[3])

# student = my_data[0]
# rank = my_data[1]

# print(student)
# print(rank)

"""1) შექმენით სია რომელშიც ჩამოწერთ თქვენთის ნაცნობ პროგრამირების ენებს, უნდა იყოს მინიმუმ 10 ელემენტი, ჯერ დაბეჭდეთ მთლიანად სია, შემდეგ კი მისი ელემენტები ცალცალკე ინდექსის გამოყენებით, კომენტარებით დაწერეთ თუ რა არის ინდექსი თქვენი აზრით"""


# my_data = [True, 2.7, "Luka", 15, True, "Luka"] # 6

# my_index = int(input('Enter item index: '))

# my_data[my_index] = "Giorgi"

# print(my_data)

# name = "Luka Gurgenidze"


# num_arr = [3, 5, 67, 12, 6, 36, 744]

# for index in range(7):
#     num_arr[index] += 1

# for i in range(10):
#     if i == 4:
#         continue
#     num_arr[i] += 1



# print(num_arr)


# 12) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)

# sentence = input()

# vowels = ["a", "e", "i", "o", "u"]

# vowel_count = 0
# for char in sentence:
#     for vowel in vowels:
#         if char == vowel:
#             vowel_count += 1

# print(vowel_count)

# games = ["Snake", "Puzzle", "Chess"]

# web_development = [
#     ["HTML", "CSS", "JS"], 
#     "Backend", 
#     "API"
# ]

# print(web_development[0][1])

grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0],
]

# print(grid[2][2])
