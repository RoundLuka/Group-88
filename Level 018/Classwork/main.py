


# while score > 0:
#     score -= 1
#     print(score)


# ინდენტაცია - დატოვილი ადგილი (სტანდარტულად 4 space) იმისთვის რომ გავიგოთ თუ რა შედის კონკრეტული კონსტრუქციის (while, for, if) კოდის ბლოკში

# if პირობითი განცხადებით ვამოწმებთ რაღაც პირობას და ის საშვალებას გვაძლევს რომ გარკვეული ინსტრუქციები (კოდის ნაწილი) გავუშვათ მხოლოდ იმ შემთხვევაში თუ პირობა არის ჭეშმარიტი

# else ბლოკში იწერება ის კოდი რომელიც უნდა შესრულდეს თუ if-ის პირობა მცდარია, else ბლოკს არ სჭირდება ცალკე პირობა, მისი პირობა არის ის რომ if უნდა იყოს მცდარი ესეიგი მისი ალტერნატივაა

# score = int(input("Enter your exam results: "))

# if score > 50:
#     print('Exam passed')
# else:
#     print("Exam failed")

# print("Student graded")

# age = 15
# if age >= 18:
#     print("Regular price")
# else:
#     print("Discount")
# print("Proceed to payment")


# exam_score = int(input("Score: "))


# # if exam_score > 90:
# #     print("A")
# # elif exam_score > 80:
# #     print("B")

# if exam_score > 90:
#     print("A")
# elif exam_score > 80:
#     print("B")
# elif exam_score > 70:
#     print("C")
# elif exam_score > 60:
#     print("D")
# elif exam_score > 50:
#     print("E")



# num = int(input("number: "))


# if (num % 2) == 0: # True -> if-ის კოდი
#     print("Even")
# else: # False -> else-ის კოდი
#     print("Odd")

# if num >= 0:
#     print("Non-Negative")
# else:
#     print("Negative")

# password = input("Enter password: ")
# username = "luka53456"

# if password != "" and password is username:
#     print("Password changed")
# else:
#     print("Please pick a different password")

# secret_code = "1234"
# attempts = 3
# pin_code = ""

# while attempts > 0:

#     pin_code = input("Enter pin: ")

#     if pin_code == secret_code:
#         print("You guessed the code")
#         break

#     attempts -= 1
#     print(f"You have {attempts} attempts left")


# 7, 9

# for num in range(5, 30):
    
#     if num == 15:
#         break

#     print(num)

# comperhension - მოკლე ჩანაწერი

num = int(input())

if num >= 0:
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Negative")

