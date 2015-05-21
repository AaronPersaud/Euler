def dsum(n):
    if n == 0:
        return 0
    else:
        return n%10 + dsum(n/10)
    
def pow():
    a = []
    for i in range(1,100):
        for j in range(1,100):
            a = a + [i**j]
    return a

def max(x):
    i = 0
    while (x!=[]):
        if (dsum(x[0]) > i):
            i = dsum(x[0])
            x = x[1:]
        else:
            x = x[1:]
    return i