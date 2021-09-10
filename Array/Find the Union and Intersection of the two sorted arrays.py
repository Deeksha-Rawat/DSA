a1=[2, 5, 6]   
a2=[4, 6, 8, 10]

n1 =len(a1)
n2 =len(a2)
intersection = []
for i in a1:
    if i in a2:
        intersection.append(i)
   
print(intersection)
    
if n1>n2:
    for i in a2:
        if i not in a1:
            a1.append(i)
    a1.sort()        
    print(a1)        
           
if n2>n1:
    for i in a1:
        if i not in a2:
            a2.append(i)
    a2.sort()        
    print(a2)    


