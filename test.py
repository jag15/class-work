total=0
count=0
while True:
	line=input('Enter number: ')
	if line == 'done':
		break
	try:
		number=float(line)
		total=total+number
		count=count+1
	except:
		print('Invalid input')
		continue
print(' ')
print('Total: ', total)
print('Count: ', count)
print('Average: ', total/count)
