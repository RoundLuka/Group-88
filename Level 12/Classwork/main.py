# print(5 < 4) # False
# print("A" != "a") # False

# num1 = 3
# num2 = 4

# print(num1 != num2)

# Logical Operators: and, or, not


# Not 
# print(not True) # False
# print(not False) # True

# Or
# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)

# # And

# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

# result = 4 > 3

# is_sunny = False
# is_raining = True
# going_outside = is_sunny and is_raining

# range(start, stop, step) - ინსტრუქცია რომელიც იღებს 3 მნიშვნელობას, საწყის პოზიციას რომელსაც იქამადე უმატებს ნაბიჯს (მესამე მნიშვნელობას რასაც გადავცემთ) სანამ არ გახდება საბოლოო მნიშვნლობის ესეიგი stop-ის (მეორე) ტოლი. თუ მხოლოდ 1 მნიშვნელობა გადავეცით range-ს მაშინ ეს ჩაითვლება stop-ად, ხოლო საწყისი იქნება 0. თუ 2 მნიშვნელობა გადავეცი პირველი იქენება საწყისი, მეორე კი საბოლოო, ნაბიჯი (step) ჩაითვლება 1


# sequenceing

# Iteration - გამეორება

# for ციკლი მეშვეობით შეგვიძლია განვიხილოთ რაიმე მიმდევრობა
# for ციკლის ინიციალიზებისას იქმენბა საიტერაციო ცვლადი
# რომელიც ამ მიმდევრობის ყველა წევრის მნიშვნელობას მიღებს

# 1, 4, 7, 
# 0, 1, 2, 3, 4, 5
numbers = range(10, 20)
for num in numbers:
    print(num) 