import random

students = [
    "დემეტრე ბაკურიძე",	
    "ზურაბ შენგელია",	
    "გიორგი კოპალეიშვილი",
    "გიორგი მეგრელი",
    "ლუკა ბენდელიანი",
    "ლუკა ლანჩავა",		
    "ნიკოლოზ ნადირაძე",	
    "ვატო ტაბატაძე",		
    "დაჩი თეთრაძე",	
]

captain1 = ["ირაკლი გერაძე",]
captain2 = ["ნიკა კანკია",]
captain3 = ["ქეთი ბაიდაური",]


random.shuffle(students)


for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))
