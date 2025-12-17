# string მეთოდები: .split, .join, .replace, .strip
# არც-ერთი მეთოდი არ ცვლის ორიგნალურ სტრინგს, აბურნებს ახალს

# split - გამოიძახება string-ზე string.split( გაყოფის-სტრინგი )
# ეს მეთოდი ერთ დიდ სტრინგს დაშლის ცალ-ცალკე ქვე სტრინგებად და შეინახავს
# თითოეულ ნაწილს სიაში ხოლო თითონ გაყოფის-სტრინგს წაშლის

# replace - გამოიძახება string (ან ცვლადზე რომელიც სტრინგს ინახავს) string.replace("old sub-string", "new sub-string"), ღებულობს 2 პარამეტრს 1. string-ის რაღაც ნაწილს რომელიც უნდა ჩავანაცლოთ და მეორე სტრინგის ნაწილს რომლითაც გვინდა რომ ჩავანაცვლოთ


# join - გამოიძახება იმ სტრინგზე string.join(string_list) რომლითაც გვინდა შევაერთოთ სიის ელემენტები (აუცილებლად სტრინგები) აბრუნებს შედეგად ერთ დიდ სტრინგს რომელშიც მოცემულია ყველა სიის ელემენტი და მათ შორის შესაერთებელი სტრინგი

# strip - გამოძახება სტრინგზე string.strip(sub-string) სტრინგს მოაშორებს დასაწყისიდან და ბოლოდან გადამბულად მოცემულ იმ ქვე სტრინგს რომელსაც გადავცემთ

# sentence = "The dog has climbed over the tree"

# words = "AAA CBC CCC CBC DDD CBC".split("CBC")
# print(words)


# words = ['The', 'dog', 'has', 'climbed', 'over', 'the', 'tree']

# sentence = "@%$@#%$@#".join(words)

# print(sentence)


# word = "Magic Spell Mana Mana Magic Spell Magic"
# word = word.replace("Mana", "Irakli")

# any_string = "!!!       stick   !   !!!1  !    !!!!!!!!!!!!!!!!!!!"
# trimmed_string = any_string.rstrip("!")
# print(any_string)
# print(trimmed_string)

# print("abc" * 3)

# print("ABC" in ["DBE", "FGE", "DBC"])

my_set = {1, 2, 3}

my_set.remove(2)

print(my_set)


# list - append, pop
# set - add, remove

my_list = [1, 2, 3]
my_list.add(4)

print(my_list)
