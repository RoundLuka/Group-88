def validate_pin(pin):
    if len(pin) != 4 or len(pin) != 6:
        return False
    
    digits = "0123456789"
    
    for char in pin:
        if char not in digits:
            return False
        
    return True

print(validate_pin('1234'))