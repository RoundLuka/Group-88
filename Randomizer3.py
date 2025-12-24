import random

students = [
    "ბაჩო ბოჯაძე",
    "დემეტრე ბაკურიძე",
    "ზურაბ შენგელია",
    "ილია ტაბატაძე",
    "ირაკლი გერაძე",
    "გიორგი ზოზიაშვილი",
    "გიორგი კოპალეიშვილი",
    "გიორგი მეგრელი",
    "ლუკა ბენდელიანი",
    "ლუკა ლანჩავა",
    "ნიკა კანკია",
    "ნიკა ცაავა",
]

captain1 = ["ნიკოლოზ ნადირაძე",]
captain2 = ["დაჩი თეთრაძე"]
captain3 = ["ვატო ტაბატაძე",]
captain4 = ["ლუკა ჩოჩუა",]
captain5 = ["ნინი ჯორბენაძე", "ქეთი ბაიდაური", "თამთა ბიწაძე",]



random.shuffle(students)


for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())
    if students: captain4.append(students.pop())
    if students: captain5.append(students.pop())

print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))
print("მეოთხე გუნდი " + str(captain4))
print("მეხუთე გუნდი " + str(captain5))

