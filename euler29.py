def powers(a,b):
	lst = []
	for i in xrange(1,a):
		for j in xrange(1,b):
			lst.append((i+1)**(j+1))
	#return lst
	d = {}
	for i in lst:
		if i not in d:
			d[i] = None
	return d


print len(powers(100,100))