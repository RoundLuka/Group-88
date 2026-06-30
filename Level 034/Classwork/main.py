# scores = (15, 18, 26, 28)

# john, jane, *others = scores

# unpacking - სიმრავლის ელემენტების ცალ-ცალკე ცვლადებში შენახვა
# ამ დროს თანიმდევრულად ხდება მნიშვნლობების მინიჭება ცვალდებზე
# პირველი ელემენტი შეინახება პირველ ცვლადში, მეორე ელემენტი მეორე ცვლადი ა.შ

# *varaible_name - rest operation რომელიც unpacking დროს ზედმეტ მნიშვნლობებს რომლებისთავაც ცვლადები არ არის შეინახავს ერთად ბოლო *variable_name rest ცვლადში, ანუ ამ ცლვადში დანარჩენი ყველა ელემენტი შეინახება სიის სახით

# print(type(others))
# print(jake)

# product = (10, "Butter", True)
# print(product)


# set-ის შექმნა შესაძლებლია 2 გზით: {}, set

# set არის დაულაგებელი მიმდევრობა რაც იმას ნიშნავს რომ ინდექსირება არ გვაქვს, არ შეიძლება დუპლიკატი (განმეორებადი) ელემენტების არსებობა, set მათ უბრალოდ წაშლის

# collectiables - string, list, tuple
# კოლექციები რომლებშიც მრავალი ელემენტი ინახება

# nums = {5, 12, 76, 12, 25}

# nums.clear()

# print(nums)

# nums.add(1)
# nums.remove(12)

# print(nums)

# elements = ["A", "D", "B", "C"]

# other_set = set(elements)

# print(other_set)

# nums1 = {1, 3, 5, 7, 8}
# nums2 = {1, 2, 7, 9}

# union = nums1.union(nums2)
# intersection = nums1.intersection(nums2)
# union.difference(intersection)

# print(nums1.union(nums2)) # გაერთიანებაში
# print(nums1.intersection(nums2)) # თანავკეთა
# print(nums2.difference(nums1)) # სხვაობა
# print(nums1.symmetric_difference(nums2)) # გაერთიანება - თანკვეთა 

# min
# max
# len
# isnumeric
# .sort - მხოლოდ სიაზე
# sorted - ყველა სიმრავლეზე მუშაობს

# dishes = ["Salad", "BBQ", "Spaghetti"]
# guests = {"Mery", "Anna", "Jonathan"}
# print(dishes[0])
# print(guests[0])

# my_numbers = [5, 151, 12, 76, 12, 56, 25]

# print(my_numbers)

