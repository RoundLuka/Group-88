import random

students = [
    "ზურაბ შენგელია",	
    "სალმე გიორგაძე",
    "ნიკოლოზ ნადირაძე",	
    "დაჩი თეთრაძე",
]

captain1 = ["ნიკა კანკია"]
captain2 = ["გიორგი მეგრელი"]        

random.shuffle(students)

for i in range(2):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
