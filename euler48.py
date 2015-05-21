def euler48():
    i = 1
    s = 0
    while (i <= 1000):
        s = s + i**i
        i = i + 1
    return s

