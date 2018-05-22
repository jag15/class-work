total=0
count=0
largest=None
smallest=None
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
	if smallest is None or number<smallest:
			smallest=number
	if largest is None or number>largest:
			largest=number
print(' ')
print('Total: ', total)
print('Count: ', count)
print('Minimum: ', smallest)
print('Maximum: ', largest)
