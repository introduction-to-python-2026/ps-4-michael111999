def split_before_each_uppercases(formula):
    x=[]
    n=0
    
    for ch in formula:
        if ch.isupper():
            x.append(formula[n:ch]
            n==len(formula[n:ch])
            
           
        
            
       

    return x
    
   
            


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
