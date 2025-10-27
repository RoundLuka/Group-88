import random

students = [
    "დემეტრე ბაკურიძე",
    "გიო ჯიღაური",
    "გიორგი კოპალეიშვილი",
    "გიორგი მეგრელი",
    "ირაკლი გერაძე",
    "ილია ტაბატაძე",
    "ქეთი ბაიდაური",
    "ლუკა ლანჩავა",
    "ნატაილია სიდამონიძე",
    "ნიკა ხაჩიძე",
    "ნიკოლოზ ნადირაძე",
    "რეზი ფერაძე",
    "ზურაბ შენგელია",
    "ნიკა ცაავა",
    "ლუკა ბენდელიანი",
    "ვატო ტაბატაძე",
    "ლუკა ჩოჩუა",
    "დათა თორია"
]

captain1 = ["ბაჩო ბოჯაძე",]
captain2 = ["ნინი ჯორბენაძე",]
captain3 = ["ზურა",]
captain4 = ["გიორგი ზოზიაშვილი",]
captain5 = ["ნანუკა ტყებუჩავა",]
captain6 = ["ნიკა კანკია",]



random.shuffle(students)


for i in range(3):
    if students: captain1.append(students.pop())
    if students: captain2.append(students.pop())
    if students: captain3.append(students.pop())
    if students: captain4.append(students.pop())
    if students: captain5.append(students.pop())
    if students: captain6.append(students.pop())


print("პირველი გუნდი " + str(captain1))
print("მეორე გუნდი " + str(captain2))
print("მესამე გუნდი " + str(captain3))
print("მეოთხე გუნდი " + str(captain4))
print("მეხუთე გუნდი " + str(captain5))
print("მეექვსე გუნდი " + str(captain6))