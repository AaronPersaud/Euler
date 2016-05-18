# lists all primes below x, and prints sum of all these numbers
def prime(x):
	lst = [2]
	a = 3
	s = 2
	print 2
	while lst[-1] < x:
		for num in lst:
			if a%num == 0:
				a += 2
				break
			elif num == lst[-1]:
				lst.append(a)
				print a
				s += a
				#x -= 1
	#print lst[:-1]
	print "sum:%s" % (s - lst[-1])

print "Enter a number"
a = raw_input()
prime(int(a))