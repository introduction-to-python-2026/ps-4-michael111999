def split_before_each_uppercases(formula):
    x=[]
    g=""
   
    
    for ch in formula:
        if g=="":
            g+=ch
        elif ch.isupper():
            x.append(g)
            g=""

            g+=ch
        else:
            g+=ch

    
            
            
       
           
        
            
       
    x.append(g)
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
