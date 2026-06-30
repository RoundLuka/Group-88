# dictionary

# key/value - გასაღები/მნიშვნელობის წყვილების ერთობლიობა
# dictionary-ში გასაღები არ შეიძლება იყოს mutable მონცამეთა ტიპი

# my_car = {
#     "brand": "Hyundai",
#     "model": "Jeep",
#     "year": 2015,
#     "price": 4000,
#     "sold": False
# }

# dictionary keys: brand, model, year, price
# dicitonary values: Hyunadi, Jeep, 2015, 4000

# my_car.clear()
# my_car.update({
#     "price": 2000,
#     "sold": True,
#     "color": "steelblue"
# })
# my_car.pop("sold")
# my_car.popitem()

# print(my_car.get("brand"))
# print(my_car.keys())
# print(my_car.values())
# print(my_car.items())

# my_car = {
#     "brand": "Hyundai",
#     "model": "Jeep",
#     "year": 2015,
#     "price": 4000,
#     "sold": False,
#     "miles": [123, 54, 12]
# }

# for key, value in my_car.items():
#     print(f"Key: {key}, Value: {value}")

# new_car = my_car.copy()
# new_car["miles"][1] = 154

# print(my_car)


# person = {
#     # keys       # values
#     "username": "Luka",
#     "hobby": "Chess",
# }

# print(person.keys())
# print("Chess" in person.values())

# numbers = [54, 25, 24, 26, 63, 45, 16, 37]
# evens = [num + 1 for num in numbers if num % 2 == 0]

#        element    defining element  # 
# for num in numbers:
#     if num % 2 == 0:
#         evens.append(num)
# [14, 15]
# print(evens)

sentence = "We are learning dictionaries & list comperhensions"

my_data = [char + "A" for char in sentence]

print(my_data)