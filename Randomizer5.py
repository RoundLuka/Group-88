import random

students = [
    "ზურაბ შენგელია",
    "ირაკლი გერაძე",
    "გიორგი კოპალეიშვილი",
    "გიორგი მეგრელი",
    "ქეთი ბაიდაური",
    "ვატო ტაბატაძე",
    "დაჩი თეთრაძე",
]

captain1 = ["დემეტრე ბაკურიძე",]
captain2 = ["ნიკა კანკია",]
captain3 = ["ნიკოლოზ ნადირაძე",]

random.shuffle(students)


for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))
