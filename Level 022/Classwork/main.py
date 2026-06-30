# # position:     1            2          3
# passwords = ["luka1234", "efdyhrf", "wreyer"]
# # index:       0           1          2
# print(passwords[1])

# # list mutable - სიის ელემნეტბის შეცვლა დაშვებულია
# passwords[0] = "irakli1234"

# print(passwords)

# username = "Luka1234"
# # index:    01234567

# for letter in username:
#     print(letter)

# for password in passwords:
#     print(password)


# my_password = "dfyer"

# passwords_data = ["luka1234", "efdyhrf", "giorgigio", "irakli1234"]

# password = input("Enter your password: ")

# password_found = False

# for saved_password in passwords_data:
#     if saved_password == password:
#         password_found = True
#         break

# if password_found:
#     print("Authorized")
# else:
#     print("Invalid login")

# first_name = input()
# last_name = input()
# hobby = input()
# employment = input()

# person = [first_name, last_name, hobby, employment]
# print(person)



# products = ["Water", "Bread", "Salt"]

# user_choice = int(input("1 - Water\n2 - Bread\n3 - Salt\nPick a product: ")) - 1

# print("Here you go " + products[user_choice])


# my_list = [True, 12, 5.4, "Hello"]
# my_list[1] = 15


# print(my_list)

# my_string = "Hello World!"

# ages = ["Stone Age", "Bronze Age", "Medival", "Renissance", "Industrial", "Modern"]
# #index:   0            1               2             3            4          5

# print(ages[1:5:2])


# numbers_array = [5, 32, 12, 76, 12, 7, 53, 7, 9,7, 745, 9, -5, 23, 46,356]

# print(numbers_array[2:4])
# slicing - მეთოდის გამოყენებით სიის/სტრინგის (seuqence - მიმდევრობის) ნაწილს ვჭრი
# slicing სინტაქსი გაქვს ინდექსინგის სინტაქსს და range-ის პარამეტრებს
# ვიყენებ მიმდევორბის (სიის/სტრინგის) სახელს, შემდეგ [] რომელშიც ვწერ საწის:საბოლოო:ნაბიჯს
# start, stop, step
# numbers_array[2: 10] = 1, 1, 1, 1, 1, 1, 1

# print(numbers_array)


username = "setert"
print(type(username[2:4]))