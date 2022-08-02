def prime_factors (n):
    a = []
    i = 2
    while n != 1:
        if n%i==0:
            n = n/i
            a.append(i)
        else:
            i += 1
            
    return a    
