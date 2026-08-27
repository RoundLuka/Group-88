import random

students = [
    "დაჩი თეთრაძე",
    "ქეთი ბაიდაური",
    "ირაკლი გერაძე",
    "გიორგი მეგრელი",
    "ნიკოლოზ ნადირაძე",
]

captain1 = ["ნიკა კანკია",]
captain2 = ["ზურაბ შენგელია",]        

random.shuffle(students)

for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
