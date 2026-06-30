# def rect(length, width):
#     area = length * width
#     perimeter = (length + width) * 2
#     return (area, perimeter)
    

# my_area, my_perimeter = rect(4, 3)
# print("Area: " + str(my_area))
# print("Permieter: " + str(my_perimeter))

# def hello(name="John"):
#     print("Welcome " + name)

# hello()

# სიმრვალე - ისეთი ცლადი რომელშიც შეიძლება მრავალი მნიშვნლობის შენახვა
# list - სიმრვალე რომელშიც შეიძლება მრავალი ელმენტის შენახვა, იქმნება [], დალაგებული
# tuple - სიმრვალე რომელიც იქმნება () და ძირითადი თვისებაა რომ არ შეგვიძლია შექმნის შემდეგ შევცვალოთ
# garden = ["Pumpkin", "Beans", "Apple", "Grapes", "Carrot"]

fruit = ("Apple", "Grapes", "Peach", "Grapes") 
# index:    0       1         2         3

# print(fruit.count("Grapes"))
# print(fruit.index("Peach"))

# def manual_count(sequence, target):
#     count = 0
#     for element in sequence:
#         if element == target:
#             count += 1
#     return count

# result = manual_count(fruit, "Grapes")
# print(result)

def manual_index(sequence, target):

    for index in range(len(sequence)):

        if sequence[index] == target:
            return index
    
    return -1, -2

print(manual_index(fruit, "Cherry"))

