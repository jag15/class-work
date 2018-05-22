nlist=[]
while True:
	line=input('Enter number: ')
	if line=='done': 
		break
	try:
		number=float(line)
	except:
		print('Invalid input')
		continue
	x=nlist.append(number)
print(' ')
print(nlist)
print('Maximum: ', max(nlist))
print('Minimum: ', min(nlist))