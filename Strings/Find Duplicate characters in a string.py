
s="hello"

hash ={}
for i in range(len(s)):
    if s[i] in hash:
        hash[s[i]]+=1
    else:
        hash[s[i]]=1

print(hash) 
for i in hash:
    if hash[i]>1:
        print(str(i)+":"+ str(hash[i]),"\n")                     





         

