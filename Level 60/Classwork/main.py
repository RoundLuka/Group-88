# nums = [7, 9, 2354, 236, 9, 9, 7]

# nums_counts = {}

# for i in nums:
#     count = 0
#     for j in nums:
#         if i == j:
#             count += 1
#     nums_counts[i] = count

# print(nums_counts)


def decode_ascii(word):
    if word[2].isdigit():
        return chr(int(word[:3])), True
    else:
        return chr(int(word[:2])), False

def decipher_this(s):
    words = s.split(" ")
    res = ""
    
    for word in words:
        first_char, is_three_digit = decode_ascii(word)
        
        length = len(word)
        if is_three_digit:
            res += first_char
            for index in range(3, length):
                char = word[index]
                
                if index == 1 or index == length - 1:
                    continue
                else:
                    res += char
                res += " "
        first_char = chr(int(word[:2]))
        res += first_char
        
        for index in range(2, len(word)):
            if index == 1 or index == len(word) - 1:
                if index == 1:
                    res += word[-1]

                if index == len(word) - 1:
                    res += word[1]
            else:
                res += word[index]
            
    return res[:-1]