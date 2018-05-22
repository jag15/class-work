hours=int(input('Enter hours: '))
rate=float(input('Enter rate: '))
if hours>40:
	pay=hours*rate*1.5
else:
	pay=hours*rate
print('Pay: ', pay)
