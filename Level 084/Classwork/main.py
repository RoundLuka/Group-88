def encode(st):
    
    if len(st) == 1:
        return f"1{st[0]}"
    
    result = ""
    
    count = 1
    for index in range(1, len(st)):
        char = st[index]
        prev_char = st[index - 1]
        
        if char == prev_char:
            count += 1
            
            if index == len(st) - 1:
                result += str(count) + prev_char
        else:
            result += str(count) + prev_char
            count = 1
    return result

print(encode("AAABBBCCCA"))