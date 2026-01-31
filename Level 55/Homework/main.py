# method - უბრალო კლასის ფუნქცია რომელიც აუიცლელბად ღებულობს პარამეტრად "self"-ს რაც გულსხმიბს იმ ობიექტს რომლებსაც მომავალში შევქმნთ კონკრეტული კლასით, ეს მეთოდი კი მხოლოდ ამ ინსტანციებზე (კონკრეტულ მაგალითზე) იქნება გამოძახებდი და მათზე შეასრულებს დავალებებს

# classmethod - ამ მეთოდის (ფუნქციის) დეკორაციას ვახდენთ @classdecorator-ით, ასევე კლასის მეთოდი აუციელბლად ღებულობს პარამეტრად "cls" რაც წაროადგენს თვითნ იმ კლასს რომელშიც ვქმნთ ამ მეთოდს, კლასის მეთოდს შეეძლება მიწვდეს კლასის ზოგად ცვლადებს და კლასისთვის დამახისათებელი ზოგადი ატრიბუტი შეცვალოს

# staticmethod - იქმნება @staticdecorator დეკორატორ ფუნქციით და მკაცრად არ მოთხევა კონკრეტული პარამეტრების მიღება, მას ვიყენებთ მაშინ როცა ის კავშირშია კლასსთან და მის ობიექტან მაგრამ ისე რომ არ გვჭირდება რომელიე ობიექტის ან კლასის ატრიბუტის გამოყენება

# დაფარული კუთვნილებები - data hiding
# protected - (_attribute) დაცული კუთვნილება რომელიც ხელმისწავდომია კლასის გარეთაც, მაგრამ ამ დროს ვიჩენთ სიფრთხილეს
# private - (__attribute) კონფიდენციალური კუთვნილება რომელიც კლასის მეთოდის გარეთ ფიზიკურად არაა ხელმისწავდომი, მისი გამოყენება შესაძლებელია მხოლოდ კლასის შიგნით 

# class Group:
#     channels = ["CW", "HW", "RS", "ST", "VC"]
#     def __init__(self, students, mentor, assistant):
#         self.students = students
#         self._mentor = mentor # protected property
#         self.__assistant = assistant # private
    
#     # getter
#     def __change_asssitant(self, new_asssitant):
#             self.__assistant = new_asssitant

#     def get_assistant(self):
#         return self.__assistant
#         self.__change_asssitant()

#     @classmethod
#     def get_channels(cls):
#         print(cls.channels)



# group_88 = Group(14, "Luka", "Giorgi")

# print(group_88.get_channels())


# Group.get_channels(group_88.__assistant)
# არასწორი გზა
# print(group_88.__assistant)
# სწორი გზა

# group_89 = Group(10, "Nika", "Zaza")

# print(group_88.students)
# print(group_88.mentor)
# print(group_88.get_assistant())


# print(group_88.__assistant)

# name mangling
# print(group_88._Group__assistant)


number = 50

if number > 0:
    print("positive")
else:
    print("negative")