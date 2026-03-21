# def rotate(data, n):
#     new_arr = [""] * len(data)
    
#     if n >= 0:
#         for index in range(len(data)):
#             current_index = index + n
#             while current_index > len(data) - 1:
#                 current_index -= len(data)

#             new_arr[current_index] = data[index]

#         return new_arr
    
#     for index in range(len(data)):
#         current_index = index - n



#         new_arr[current_index] = data[index]    

    
#     return new_arr

# print(rotate([1, 2, 3, 4, 5], -1))


data = 10

#          
for letter in "ABCDEF":
    for num in range(6):
        print(num, letter)