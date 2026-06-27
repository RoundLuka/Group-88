import random

students = [
    "დაჩი თეთრაძე",
    "ნიკოლოზ ნადირაძე",
    "გიორგი კოპალეიშვილი",
    "გიორგი მეგრელი",
    "ირაკლი გერაძე",
]

captain1 = ["ნიკა კანკია",]
captain2 = ["ზურაბ შენგელია",] 
captain3 = ["ქეთი ბაიდაური",] 

random.shuffle(students)

for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))