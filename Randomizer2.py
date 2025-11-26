import random

students = [
    "დემეტრე ბაკურიძე",
    "ილია ტაბატაძე",
    "ირაკლი გერაძე",
    "გიორგი ზოზიაშვილი",
    "ლუკა ბენდელიანი",
    "ლუკა ლანჩავა",
    "ლუკა ჩოჩუა",
    "ნიკა კანკია",
    "ნიკა ცაავა",
    "ნიკოლოზ ნადირაძე",
    "ვატო ტაბატაძე",
    "ლუკა კირვალიძე",
    "რეზი ფერაძე",
]

captain1 = ["გიორგი მეგრელი"]
captain2 = ["გიორგი კოპალეიშვილი"]
captain3 = ["ბაჩო ბოჯაძე",]
captain4 = ["ზურაბ შენგელია"]
captain5 = ["ზურა ჯაყელიძე",]
captain6 = ["ქეთი ბაიდაური", "ნინი ჯორბენაძე",  "ნანუკა ტყებუჩავა", "ნატაილია სიდამონიძე","თამთა ბიწაძე",]



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
print("მეექვსე გუნდი " + str(captain6))