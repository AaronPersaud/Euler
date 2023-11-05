import math

def isPrime(n):
	for i in range (2, math.ceil(n**0.5)+1):
		if n % i == 0:
			return False
	return True

def rotate(n):
	perms = [n]
	for i in range(len(str(n))-1):
		s = str(n)
		start = s[:-1]
		end = s[-1]
		n = int(end + start)
		perms.append(n)
	return perms

i = 3
primes = [2]

while i < 1000000:
	if isPrime(i):
		primes.append(i)
	i += 2

circular = []

for p in primes:
	perms = rotate(p)
	flag = 1
	for perm in perms:
		if perm not in primes:
			flag = 0
			break
	if flag:
		circular.append(p)

print(len(circular))



