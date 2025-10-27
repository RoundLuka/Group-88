# for ციკლის სტრუქტურა
# 1. for
# 2. საიტერაციო ცვლადი
# 3. in ოპერატორი
# 4. მიმდევრობა
# 5. ორწერტილი :
# 6. კოდის ბლოკი

# DRY - Dont Repeat Yourself

# range(10) - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9


# for num in range(10):
#     print("Hello")
#     print("Hello")


# while ციკლის სტრუქტურა
# 1. while
# 2. პირობა და ორწერტილი
# 3. კოდის ბოლკი

# counter = 0
# while counter < 10:
#     print(counter)
#     counter += 1

# print("Loop ended")

# pin code: 1234 | 123456



pin_code = "4531"

code = ""

while code != pin_code:
    code = input("Enter pin code: ")

print("Pin correct, Authorised!")