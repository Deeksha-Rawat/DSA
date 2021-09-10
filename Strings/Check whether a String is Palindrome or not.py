# using recursion

def palin(s):
    if len(s)<=1:
        return True
    else:
        if s[0]==s[-1]:
            return palin(s[1:-1])  
            
        else:
            return False    
s="madam"
if palin(s)==True:
    print("its palindrome")
else:
    print("its not")                
        
      
      
      
# without recusion

def palin(s):
    n=len(s)

    for i in range(n//2):
        if s[i]!=s[n-i-1]:
            return False
    return True


s="madam"
print(palin(s))
      
