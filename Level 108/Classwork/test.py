def is_merge(s, part1, part2):
    
    part1_arr = [-1]
    part2_arr = [-1]
    
    for index in range(len(part1)):
        
        char = part1[index]
        
        try:
            s_index = s.index(char)
        except: 
            return False
        
        biggest_index_yet = max(part1_arr)
        
        if s_index < biggest_index_yet:
            return False
        
        part1_arr.append(s_index)
        
        try:
            s_before = s[:s_index]
            s_after = s[s_index + 1:]   
            s = s_before + s_after
        except:
            s = ""
            
    for index in range(len(part2)):
        
        char = part2[index]
        
        try:
            s_index = s.index(char) 
        except:
            return False
        
        biggest_index_yet = max(part2_arr)
        
        if s_index < biggest_index_yet:
            return False
        
        part2_arr.append(s_index)
        
        try:
            s_before = s[:s_index]
            s_after = s[s_index + 1:]   
            s = s_before + s_after
        except:
            s = ""
        
    return s == ""

print(is_merge("Can we merge it? Yes, we can!", "C e  es an", "anwe mrgeit?Y, wec!"))