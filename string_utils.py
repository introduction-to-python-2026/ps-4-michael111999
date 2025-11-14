def split_before_each_uppercases(formula):
    x = ""
    y = ""
    
    
    for ch in formula:
        if ch.isupper():
            
           
        
            y += ch
        elif ch.isalpha():
            x += ch

    return x, y
    
   
            


def split_at_first_digit(formula):
    x=""
    y = ""
    digt=False
    
    
    for ch in formula:
        if ch.isdigit():
            x+=ch
            digt=True
            
        
            
       
            
        elif ch.isalpha():
            y += ch
    if digt==False:
        x+="1"
    return y, int(x)
