"""1) დაწერეთ დეკორატორ ფუნქცია, რომელიც იმუშავებს ქეშირებაზე.
გაქვთ ფუნქციები, რომელიც აბრუნებს რიცხვის კვადრატს, კუბს და მეოთხე ხარისხს
(სამივე ცალ-ცალკე აღწერეთ), დეკორატორმა კი უკვე გამოთვლილი შედეგი პირდაპირ დააბრუნოს
და აღარ უნდა იყოს საჭირო თავიდან გამოთვლა."""


# def cache_decorator(func):

#     cache = {}

#     def wrapper(*args):
#         if args not in cache:
#             cache[args] = func(*args)
#             print("გამოთვალა")
#         else:
#             print("შენახული გამოიყენა")
#         return cache[args]

#     return wrapper

# @cache_decorator
# def square(n, m):
#     return n * m 

# def cube(n):
#     return n ** 3

# def power4(n):
#     return n ** 4

# print(square(10, 5))

"""3) 
დაწერეთ დეკორატორ ფუნქცია, რომელიც ტექსტს რევერსულად შეაბრუნებს. 
გაქვთ ფუნქცია, რომელსაც გადაეცემა სიტყვების სია. ფუნქციამ ეს სიტყვები უნდა გააერთიანოს, 
მიღებული წინადადება კი დეკორატორმა რევერსულად შეაბრუნოს."""

def reverse_text(func):
    def wrapper(words):
        return func(words[::-1])
    return wrapper

@reverse_text
def join_words(words):
    return ' '.join(words)

print(join_words(['აი,',  'რა', 'მზის', 'სიზმარია,']))
join_words(['აირევი,', 'ივერია...'])
join_words(['აი,',  'დროშა,', 'აშორდია,'])
join_words(['აერების',  'სიბერეა.'])

'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც შეინახავს ისტორიას. 
გაქვთ ფუნქცია, რომელიც ორ რიცხვს კრებს, დეკორატორი კი ბოლო ხუთ გამოთვლას ინახავს 
და მთავარ შედეგთან ერთად პრინტავს.
'''

def keep_history(func):
    def wrapper(*args, **kwargs):
        func(args, kwargs)

    return wrapper

@keep_history
def add(a, b):
    return a + b

add(2, 3)
add(10, 5)
add(7, 8)
add(1, 9)
add(4, 6)
add(20, 30)