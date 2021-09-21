s1="abcd"
s2="cdab"
temp = s1+s1
if len(s1)!=len(s2):
    print(False)
if s2 in temp:
    print(True)
else:
    print(False)
