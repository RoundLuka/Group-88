import random

students = [
    "ზურაბ შენგელია",
    "ირაკლი გერაძე",
    "გიორგი კოპალეიშვილი",
    "ვატო ტაბატაძე",
    "დემეტრე ბაკურიძე",
    "ნიკა კანკია",
    "ნიკოლოზ ნადირაძე",
]

captain1 = ["გიორგი მეგრელი"]
captain2 = ["ქეთი ბაიდაური"]
captain3 = ["დაჩი თეთრაძე"]

random.shuffle(students)


for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))
