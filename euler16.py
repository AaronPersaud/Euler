def dsum(n):
    if n == 0:
        return 0
    else:
        return n%10 + dsum(n/10)

dsum(2**1000)