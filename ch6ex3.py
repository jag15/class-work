def count(w,l):
	total=0
	for letter in w:
		if letter==l:
			total=total+1
	return total

word=input('Enter the word to search: ')
letter=input('Enter the letter to search: ')
answer=count(word,letter)
print(answer)
