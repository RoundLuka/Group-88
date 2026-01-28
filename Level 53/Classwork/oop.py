# Objected Oriented Programming

# class Fighter:
#     def __init__(self, name, health, damage, speed):
#         self.name = name
#         self.health = health
#         self.damage = damage
#         self.speed = speed
    
#     # method
#     def heal_up(self):
#         self.health += 100

# class Medic:
#     def heal_up(self):
#         print("healed up")

# # instance - ინსტანცია წარმოადგენს კლასის კონკრეტულ ერთ-ერთ 
# samurai = Fighter("Samurai", 200, 40, 25)
# ninja = Fighter("Ninja", 80, 60, 60)
# doctor = Medic()

# samurai.heal_up()
# samurai.heal_up()
# samurai.heal_up()

# doctor.heal_up()

# print(samurai.health)

# კლასი ზოგადი ცნება, რომლითაც ვაგებთ ერთგვარ ელემენტებს
class Gamer:
    count = 0
    def __init__(self, game, time_played):
        self.favourite_game = game
        self.hours = time_played
        Gamer.count += 1
    
    def play(self):
        self.hours += 1

    @classmethod
    def count_gamers(cls):
        print(cls.count)

# კლასის კონკრეტულ წარმომადგენებლს ვუწოდებთ ინსტანციებს/ობიექტი
# irakli = Gamer("RD2", 100)
# luka = Gamer("Warband", 300)
# zurabi = Gamer("Roblox", 200)

# luka.play()
# luka.play()
# luka.play()

# luka.play()
# Gamer.play(luka)

# "wetwtwtw".lower()

# def any():
#     pass

# print(any)

class Fighter:
    def __init__(self, health, damage, speed):
        self.health123 = health + 100
        self.damage = damage
        self.speed = speed

class Archer(Fighter):
    def __init__(self, health, damage, speed, range, reload):
        super().__init__(health, damage, speed)
        self.range = range
        self.reload = reload

wizard = Archer(30, 50, 20, 100, 22)

print(wizard.health123)
