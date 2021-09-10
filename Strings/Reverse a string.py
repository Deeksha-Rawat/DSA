s = ["h","e","l","l","o"]
n=len(s)
i=0
while(i<=n//2):
    s[i],s[n-i-1]=s[n-i-1],s[i]
    i+=1
print(s)
