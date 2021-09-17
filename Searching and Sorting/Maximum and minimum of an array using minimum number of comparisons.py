if n==1:
        min = a[0]
        max = a[0]
        return min
        return max
    else:
        max=a[1]
        min=a[0]
    for i in range(n):  
        if max<a[i]:
            max=a[i]
        if min>a[i]:
            min=a[i]
    
    return (min,max)
    
