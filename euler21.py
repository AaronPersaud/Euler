import math
# lists all primes below x
def prime(x):
	lst = [2]
	a = 3
	while lst[-1] < x:
		for num in lst:
			if a%num == 0:
				a += 2
				break
			elif num == lst[-1]:
				lst.append(a)
	return lst[:-1]

primes = prime(10000)

def f(n):
	lst = [1]
	for i in xrange(2,int(math.ceil(n**0.5))+1):
		if i*i == n:
			lst.append(i)
		elif n%i == 0:
			lst.append(i)
			lst.append(n/i)
	return sum(lst)

def fun():
	nums = []
	pairs = {}
	for i in xrange(1,10001):
		if i not in primes:
			pairs[i] = f(i)
	for i in xrange(1,10001):
		if f(i) in pairs and pairs[f(i)] == i and f(i) != i:
			nums.append(i)
			nums.append(f(i))
	print sum(nums)/2

fun()



		
