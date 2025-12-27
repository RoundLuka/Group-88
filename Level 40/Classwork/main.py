# grid = [
#     [0, 0, 0],
#     [0, 0, 0],
#     [0, 1, 0],
# ] 

# 3
# 0, 1, 2

# for x in range(len(grid)):
    
#     current_list = grid[x]

#     for y in range(len(current_list)):
#         if current_list[y] == 1:
#             print([x, y])

# letters = ["A", "B", "C"]

# print("".join(letters))

# დაწერეთ ფუნქცია რომელიც upper_case-იდან გადაიყვანს ელემენტს lower_case-ში
# upper & lower მეთოდების გამოყენების გარეშე

# 01101

# ABC 

# A
# -
# 

# 1011101


# encoding functions
# ord, chr

def case_swap(word):

    swapped = ""
    
    for char in word:
        code = ord(char)

        if 65 <= code <= 90:
            new_code = code + 32
            swapped += chr(new_code)
        elif 97 <= code <= 122:
            new_code = code - 32
            swapped += chr(new_code)
        else:
            swapped += char
    
    return swapped

# Test Case
print(case_swap("aBcD")) # "aBcD" -> 'AbCd'
print(case_swap("DYsdtgerFWESTW^@@^Dsd&()):twW46rwsta654"))

# print(ord("F")) 
# print(chr(70))

# ord - ღებულობს სიმბოლოს და გვაძლევს ასკიში მის შესაბამის კოდს
# chr - ღებულობს ასკის კოდს და გიბრუნებთ ასკიში კოდის შესაბმის სიმბოლოს
