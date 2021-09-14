def sun(a,n):
    sum=0
    s=[]
    for i in range(n):
        sum+=a[i]

        if sum==0 or sum in s:
            return True
    return False
