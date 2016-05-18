def a_insert(c,lst):
	a = []
	for perm in lst:
		for i in xrange(len(perm) + 1):
			a.append(perm[:i] + c + perm[i:])
	return a

#prints all permutations of a given string
def permute(word):
	if len(word) == 1:
		return [word]
	else:
		return a_insert(word[0], permute(word[1:]))

a = permute('0123456789')
print sorted(a)[999999]