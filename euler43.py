#check if a given number meets the criteria
def check(x):
	i = str(x)
	a = int(i[1:4]) % 2 == 0
	b = int(i[2:5]) % 3 == 0
	c = int(i[3:6]) % 5 == 0
	d = int(i[4:7]) % 7 == 0
	e = int(i[5:8]) % 11 == 0
	f = int(i[6:9]) % 13 == 0
	g = int(i[7:10])% 17 == 0
	return a and b and c and d and e and f and g

#helper function for permute that inserts a character into all places of a string
def a_insert(c,lst):
	l = []
	for i in xrange(len(lst)):
		for j in xrange(len(lst[i]) + 1):
			l.append(lst[i][0:j] + c + lst[i][j:])
	return l

#finds all permutations of a given string
def permute(word):
	if len(word) == 1:
		return [word]
	else:
		return a_insert(word[0],permute(word[1:]))

#set we're working with
numbers = permute('1234567890')

#for loop that finds all 0 to 9 pandigital numbers that meets critea
newl = []
for i in numbers:
	if check(i):
		newl.append(i)
print sum([int(x) for x in newl])