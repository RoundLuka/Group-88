import random

students = [
    "დაჩი თეთრაძე",
    "ნიკა კანკია",
    "ზურაბ შენგელია",
    "ქეთი ბაიდაური",
    "ირაკლი გერაძე",
]

captain1 = ["გიორგი მეგრელი",]
captain2 = ["ნიკოლოზ ნადირაძე",]        

random.shuffle(students)

for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
