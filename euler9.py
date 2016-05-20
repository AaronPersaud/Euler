a = []
for i in xrange(1000):
	a.append(i+1)
#print a
d = {}
for i in a:
	d[i**2] = None
#print d
for i in xrange(1,500):
	for j in xrange(1,500):
		if i**2 + j**2 in d:
			print i + j + (i**2 + j**2)**0.5, i, j
print 425*375*200
