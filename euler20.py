def factorial(n):
    assert(n>=0)
    product = 1
    while (n!=0):
        product = product*n
        n = n - 1
    return product

def dsum(n):
    if n == 0:
        return 0
    else:
        return n%10 + dsum(n/10)