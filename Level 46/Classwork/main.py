# events = ["WW2", "Cold War", "WW1"]

# index = int(input("Index: "))

# if index > len(events) - 1:
#     raise IndexError("Index wont be in the list")

# try - ბლოკში იწერება ის კოდი რომელზეც ეჭვი გვაქვს რომ შეიძლება მოხდეს Error
# except - (უთითეთ error-ს) ბლოკში იწერება ის დავალება რომელიც უნდა შესრულდეს თუ try ბლოკში აღმოჩნდა error
# else - ეშვება მხოლოდ და მხოლოდ მაშინ როდესაც try ბლოკი გაეშვა უშეცდომოდ
# finally - აქ მოცემული კოდი ეშვება ყველა შემთხვეაში

# try:
#     print(events[index])
# except IndexError:
#     print("Given index isn't avaliable in the list")
# else:
#     print("Event successfuly found")
# finally:
#     print("Code block of finally, will execute regradless")

# try:
#     index = int(input())
#     print(qwer[index])
# except NameError:
#     print("Something went wrong")

# print("Code contines running")

# print("wetwRYERYEatEwtetew".isalpha())



    