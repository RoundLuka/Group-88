import random

students = [
    "ირაკლი გერაძე",
    "გიორგი კოპალეიშვილი",
    "დემეტრე ბაკურიძე",
    "ნიკა კანკია",
    "გიორგი მეგრელი",
    "ქეთი ბაიდაური"
]

captain1 = ["დაჩი თეთრაძე"]
captain2 = ["ნიკოლოზ ნადირაძე",]
captain3 = ["ზურაბ შენგელია",]

random.shuffle(students)

for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))