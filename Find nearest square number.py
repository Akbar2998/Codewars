def nearest_sq(n):
    a = int(n**(1/2))
    b = (n**(1/2))
    if b - a >= (1/2):
        return (a+1)**2
    else:
        return a**2
