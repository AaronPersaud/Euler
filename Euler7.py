def lf(i):
    lpf = 1
    a = 1
    while (a < i):
        if (i%a == 0):
            lpf = a
            a=a+1
        else:
            a=a+1
    return lpf

def euler7(i):
    p = 2
    a = 2
    while(i > 0) :
        if (lf(a)==1):
            p = a
            i=i-1
            a=a+1
        else:
            a=a+1
    return p


##euler 7 5000 = 48611