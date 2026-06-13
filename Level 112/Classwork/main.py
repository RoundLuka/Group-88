def presses(phrase):
#     press_count = {
#         ["1"]: 1,
#         'A': 1,
#         'B': 2,
#         "C": 3,
#         "2": 4,
#         'D': 1,
#         'E': 2,
#         "F": 3,
#         "3": 4,
#         "G": 1,
#         "H", 2:
#         "I": 3,
#         "4": 4,
#         "J": 1,
#         "K": 2,
#         "L": 3,
        
#     }
    
    button_groups = ["|1", "|abc2", "|def3", "|ghi4", "|jkl5", "|mno6", "|pqrs7", "|tuv8", "|wxyz9", "|*", "|#", "| 0"]
    
    total_btns = 0
    for char in phrase:
        char = char.lower()
        for pack in button_groups:
            if char in pack:
                total_btns += pack.index(char)
    return total_btns

def grabscrab(said, possible_words):
    
    
    result = []
    for word in possible_words:
        if sorted(word) == sorted(said):
            result.append(word)
    return result
            

def knight_vs_rook(knight, rook):

    cols = "ABCDEFGH"
    
    knight_row, knight_col = knight
    rook_row, rook_col = rook
    
    if abs(knight_row - rook_row) == 1 and abs(cols.index(knight_col) - cols.index(rook_col)) == 2 or abs(knight_row - rook_row) == 2 and abs(cols.index(knight_col) - cols.index(rook_col)) == 1:
        return "Knight"
    elif knight_row == rook_row or knight_col == rook_col:
        return "Rook"
    return 'None'