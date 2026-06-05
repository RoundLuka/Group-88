'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც იმუშავებს ქეშირებაზე.
გაქვთ ფუნქციები, რომელიც აბრუნებს რიცხვის კვადრატს, კუბს და მეოთხე ხარისხს
(სამივე ცალ-ცალკე აღწერეთ), დეკორატორმა კი უკვე გამოთვლილი შედეგი პირდაპირ დააბრუნოს
და აღარ უნდა იყოს საჭირო თავიდან გამოთვლა.

'''
#
def cache(func):
    cch = {}
    def wrapper(n):
        if n not in cch:
            cch[n] = func(n)
            print(f'გამოთვლა - {func.__name__}({n}) = {cch[n]}')
        else:
            print(f'კეში - {func.__name__}({n}) = {cch[n]}')
        return cch[n]

    return wrapper

# 5 -> 25
@cache
def square(n):
    return n ** 2

@cache
def cube(n):
    return n ** 3

@cache
def fourth_power(n):
    return n ** 4
#
print('--- square ---')
square(4)
square(4)
square(7)
print('--- cube ---')
cube(3)
cube(3)
print('--- fourth_power ---')
fourth_power(2)
fourth_power(2)


'''დაწერეთ დეკორატორ ფუნქცია, რომელიც მონაცემთა სტრუქტურას გადააქცევს კორტეჟად.
გაქვთ ფუნქციები, რომელიც შემთხვევითობის პრინციპით აგენერირებს 10 ელემენტიან სიას
და სიმრავლეს (ორივე ცალ-ცალკე აღწერეთ), ხოლო დეკორატორი მას გადააქცევს კორტეჟად.'''

#
# import random
# def to_tuple(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print(f'{func.__name__} ფუნქციის საწყისი ფორმა: {result}')
#         converted = tuple(result)
#         print(f'{func.__name__} - {type(result).__name__} → tuple: {converted}')
#         return converted
#     return wrapper
#
# @to_tuple
# def generate_list():
#     return random.sample(range(1, 101), 10)
# @to_tuple
# def generate_set():
#     return set(random.sample(range(1, 101), 10))
#
# print('--- სია → კორტეჟი ---')
# print(generate_list())
# print('--- სიმრავლე → კორტეჟი ---')
# print(generate_set())



'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც ტექსტს რევერსულად შეაბრუნებს. 
გაქვთ ფუნქცია, რომელსაც გადაეცემა სიტყვების სია. ფუნქციამ ეს სიტყვები უნდა გააერთიანოს, 
მიღებული წინადადება კი დეკორატორმა რევერსულად შეაბრუნოს.
'''

# def reverse_text(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         reversed_result = result[::-1]
#         print(f'ორიგინალი: - "{result}"')
#         print(f'რევერსირებული: "{reversed_result}"')
#         return reversed_result
#     return wrapper
#
#
# @reverse_text
# def join_words(words):
#     return ' '.join(words)
#
# join_words(['აი,',  'რა', 'მზის', 'სიზმარია,'])
# join_words(['აირევი,', 'ივერია...'])
# join_words(['აი,',  'დროშა,', 'აშორდია,'])
# join_words(['აერების',  'სიბერეა.'])


'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც შეინახავს ისტორიას. 
გაქვთ ფუნქცია, რომელიც ორ რიცხვს კრებს, დეკორატორი კი ბოლო ხუთ გამოთვლას ინახავს 
და მთავარ შედეგთან ერთად პრინტავს.
'''
#
# def keep_history(func):
#     history = []
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         history.append(f'{args[0]} + {args[1]} = {result}')
#
#         if len(history) > 5:
#             history.pop(0)
#
#         print(f'შედეგი: {args[0]} + {args[1]} = {result}')
#         print('ბოლო გამოთვლები:')
#         for i, record in enumerate(history, 1):
#             print(f'  {i}. {record}')
#         print()
#
#         return result
#     return wrapper
#
#
# @keep_history
# def add(a, b):
#     return a + b
#
# add(2, 3)
# add(10, 5)
# add(7, 8)
# add(1, 9)
# add(4, 6)
# add(20, 30)


'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც ტექსტს დაამუშავებს და გარკვეულ სიტყვებს „გაფილტრავს“. 
გაქვთ ფუნქცია, რომელსაც გადაეცემა ტექსტი.  ფუნქციამ უნდა დაითვალოს ტექსტში ასო-ბგერების რაოდენობა. 
დეკორატორმა კი - ტექსტში შემავალი კონკრეტული სიტყვები (თქვენი გემოვნებით) ჩაანაცვლოს *** სიმბოლოებით.
'''

# def filter_words(func):
#     banned = ['ზარმაცი', 'სულელი']
#     def wrapper(text):
#         filtered_text = text
#         for word in banned:
#             filtered_text = filtered_text.replace(word, '***')
#
#         result = func(filtered_text)
#
#         print(f'ორიგინალი ტექსტი:  "{text}"')
#         print(f'გაფილტრული ტექსტი: "{filtered_text}"')
#         print(f'ასო-ბგერების რაოდენობა: {result}')
#
#         return result
#     return wrapper
#
# @filter_words
# def count_letters(text):
#     return sum(1 for char in text if char.isalpha())
#
# print('--- მაგალითი 1 ---')
# count_letters('გარფილდი ძალიან ზარმაცი ფისოა')
# print('--- მაგალითი 2 ---')
# count_letters('ოდი ძალიან სულელი ძაღლია')
# print('--- მაგალითი 3 ---')
# count_letters('პითონი საუკეთესო და საინტერესო ენაა')


'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც შეცვლის ფუნქციის გამოთვლილ შედეგს. 
გაქვთ ფუნქციები, რომლებიც ორ რიცხვზე აკეთებენ ოთხ საბაზისო არითმეტიკულ ოპერაციას (ოთხივე ცალ-ცალკე აღწერეთ). 
დეკორატორის დანიშნულებაა, თუ ფუნქციის შედეგი ლუწია გაამრავლოს ორზე, 
ხოლო თუ კენტი - გაამრავლოს ორზე და დაუმატოს ერთი.
'''

# def modify_result(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#
#         if isinstance(result, float) and result.is_integer():
#             result = int(result)
#
#         if isinstance(result, int):
#             modified = result * 2 if result % 2 == 0 else result * 2 + 1
#         else:
#             modified = result
#
#         print(f'ოპერაცია: - {func.__name__}({args[0]}, {args[1]})')
#         print(f'ორიგინალი შედეგი: - {result}')
#         print(f'შეცვლილი შედეგი: - {modified}')
#         print()
#
#         return modified
#     return wrapper
#
#
# @modify_result
# def add(a, b):
#     return a + b
# @modify_result
# def subtract(a, b):
#     return a - b
# @modify_result
# def multiply(a, b):
#     return a * b
# @modify_result
# def divide(a, b):
#     return a / b if b != 0 else 'ნულზე გაყოფა არ შეიძლება'
#
# print('--- შეკრება ---')
# add(3, 5)
# add(4, 3)
# print('--- გამოკლება ---')
# subtract(10, 4)
# subtract(9, 3)
# print('--- გამრავლება ---')
# multiply(3, 4)
# multiply(3, 5)
# print('--- გაყოფა ---')
# divide(10, 2)
# divide(10, 4)
# divide(10, 0)


'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც ტექსტს შემთხვევითობის პრინციპით შეცვლის ასო-ბგერის რეგისტრს. 
გაქვთ ფუნქცია, რომელსაც გადაეცემა სიტყვების კორტეჟი. 
ფუნქციამ ეს სიტყვები უნდა გააერთიანოს, მიღებული წინადადება კი დეკორატორმა შეცვალოს.
'''

# import random
# def random_case(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         modified = ''.join(
#             char.upper() if random.choice([True, False]) else char.lower()
#             for char in result)
#
#         print(f'ორიგინალი: "{result}"')
#         print(f'შეცვლილი:  "{modified}"')
#
#         return modified
#     return wrapper
# @random_case
# def join_words(words):
#     return ' '.join(words)
#
# join_words(('Love', 'me', 'Feed', 'me', 'Never', 'Leave', 'me'))



'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც შეინახავს ისტორიას. 
გაქვთ ფუნქცია, რომელიც ორ რიცხვს ამრავლებს ერთმანეთზე. 
დეკორატორი კი ბოლო გამოთვლის მიხედვით ცვლის შედეგს. 
თუ ბოლო გამოთვლა ლუწია, მიმდინარე შედეგი უნდა დააბრუნოს კენტი. 
თუ მიმდინარე შედეგი ლუწია 1-ს ამატებს, ხოლო თუ კენტი - უცვლელად ტოვებს. 
დეკორატორმა ყველა გამოთვლა უნდა დააბრუნოს ლუწი-კენტი-ლუწი-კენტი პრინციპით.
'''

# def history_parity(func):
#     history = []
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if not history:
#             modified = result
#         else:
#             last = history[-1]
#             if last % 2 == 0:
#                 modified = result if result % 2 != 0 else result + 1
#             else:
#                 modified = result if result % 2 == 0 else result + 1
#
#         history.append(modified)
#
#         print(f'გამრავლება:    {args[0]} * {args[1]} = {result}')
#         if len(history) > 1:
#             print(f'ბოლო შედეგი:   {history[-2]} → {'ლუწი' if history[-2] % 2 == 0 else 'კენტი'}')
#         print(f'შეცვლილი:      {modified} → {'ლუწი' if modified % 2 == 0 else 'კენტი'}')
#         print(f'ისტორია:       {history}')
#         print()
#
#         return modified
#     return wrapper
#
# @history_parity
# def multiply(a, b):
#     return a * b
#
# multiply(3, 4)
# multiply(5, 4)
# multiply(3, 7)
# multiply(6, 4)
# multiply(5, 5)


'''
დაწერეთ დეკორატორ ფუნქცია, რომელიც ინფორმაციას შეინახავს ფაილში. 
გაქვთ ფუნქცია, რომელსაც გადაეცემა ტექსტი და დამატებით ერთი არგუმენტი, 
რომელიც განსაზღვრავს ტექსტი მაღალ რეგისტრში უნდა გადავიდეს თუ დაბალში. 
მიღებული შედეგი კი დეკორატორმა ფაილში უნდა ჩაწეროს.
'''

# def save_to_file(func):
#     filename = 'results.txt'
#     def wrapper(text, uppercase):
#         result = func(text, uppercase)
#         mode = 'მაღალ' if uppercase else 'დაბალ'
#
#         with open(filename, 'a', encoding='utf-8') as f:
#             f.write(result)
#             f.write('\n')
#
#         print(f'ორიგინალი: - "{text}"')
#         print(f'შედეგი {mode} რეჟიმში: - "{result}"')
#         return result
#     return wrapper
#
# @save_to_file
# def change_case(text, uppercase):
#     return text.upper() if uppercase else text.lower()
#
# change_case('"There are all kinds of courage," said Dumbledore, smiling.', True)
# change_case('"It takes a great deal of bravery to stand up to our enemies, ', False)
# change_case('but just as much to stand up to our friends.', False)
# change_case('I therefore award ten points to Mr. Neville Longbottom."', True)