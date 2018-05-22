def chop(c):
	del c[len(c)-1]
	del c[0]
letters =['a', 'b', 'c', 'd', 'e']
chop(letters)
print(letters)

def middle(m):
	return m[1:len(m)-1]
letters = ['a', 'b', 'c', 'd', 'e']
rest = middle(letters)
print(rest)
print(letters)
