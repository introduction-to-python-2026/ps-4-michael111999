def split_before_each_uppercases(formula):
    x = ""
    y = ""
    uppercase_found = False
    
    for ch in formula:
        if not uppercase_found and ch.isupper():
            uppercase_found = True
            y += ch
        elif uppercase_found:
            y += ch
        else:
            x += ch

    return x, y
    
   
            


def split_at_first_digit(formula):
    x = ""
    y = ""
    digit_found = False
    
    for ch in formula:
        if not digit_found and ch.isdigit():
            digit_found = True
            y += ch
        elif digit_found:
            y += ch
        else:
            x += ch

    return x, y
