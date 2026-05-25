import random

students = [
    "დემეტრე ბაკურიძე",
    "ნიკა კანკია",
    "ქეთი ბაიდაური",
    "დაჩი თეთრაძე",
    "ნიკოლოზ ნადირაძე",
    "ზურაბ შენგელია",
]

captain1 = ["გიორგი კოპალეიშვილი",]
captain2 = ["ირაკლი გერაძე",] 
captain3 = ["გიორგი მეგრელი",] 

random.shuffle(students)

for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))