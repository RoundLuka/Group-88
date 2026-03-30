def rotate(data, n):
    result = [""] * len(data)
    
    if n >= 0:
        
        for index in range(len(data)):
            new_index = index + n
            
            while new_index > len(data) - 1:
                new_index -= len(data)
            
            result[new_index] = data[index]
    
    for index in range(len(data)):
        new_index = index + n
        
        while new_index < -len(data):
            new_index += len(data)
        result[new_index] = index
    
    return result

print(rotate([1, 2, 3, 4, 5], 1))