def is_a_valid_message(message):
    digits = "0123456789"
    count = 0
    current_digit = None
    
    for char in message:
        if char in digits:
            if not current_digit:
                pass
            else:
                if int(current_digit) != count:
                    return False
                count = 0
            
            current_digit = char
        else:
            count += 1
    return True

print(is_a_valid_message("3hey5hello2hi")) # True