"""დავალება:
შექმენით პროგრამა, რომელიც:
•	კლავიატურიდან მიიღებს რამდენიმე წინადადებას (Enter-ით გამოყოფილი)
•	შეინახავს sentences.txt ფაილში (ყოველი წინადადება ცალკე ხაზზე)
•	წაიკითხავს ფაილს და შეასრულებს შემდეგ ოპერაციებს:
- დათვლის თითოეულ ხაზზე სიტყვების რაოდენობას
- იპოვის ყველაზე გრძელ წინადადებას (სიტყვების რაოდენობით)
- ამოშლის ყველა სპეციალურ სიმბოლოს (!,?.,;:)
•	დამუშავებული ტექსტი შეინახოს clean_text.txt ფაილში
•	კონსოლში გამოიტანოს: წინადადებების რაოდენობა და ყველაზე გრძელი წინადადება
"""

sentence = "1"
sentences = []

while sentence != "":
    sentence = input("Enter a sentence: ")
    sentences.append(sentence)
sentences.pop()


file_name = "sentences.txt"

with open(file_name, "w", encoding="utf-8") as file:
    for sentence in sentences:
        file.write(sentence + "\n")

with open(file_name, "r", encoding="utf-8") as file:
    lines = file.readlines()

    word_counts = []
    
    for line in lines:
        line = line.strip()

        words = line.split(' ')
        word_counts.append(len(words))
    
    longest_line = max(word_counts)
    longest_index = word_counts.index(longest_line)
    longest = lines[longest_index]

with open("clean.txt", "w", encoding="utf-8") as file:
    new_lines = []
    for line in lines:
        line = line.strip()
        new_line = ""
        for char in line:
            if char.isalpha() or char in "0123456789":
                new_line += char
        new_lines.append(new_line)
    
    for new_line in new_lines:
        file.write(new_line + "\n")

print(f"Lines word count: {word_counts}")
print(f"Longest line: {longest}")

my_data = {
    "A": 10,
    "B": 20
}