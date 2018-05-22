try:
	score=float(input('Enter score: '))
	if score>=0.0 and score<=1.0:
		pass
		if score>=0.9 and score<=0.99:
			print('A')
		if score>=0.8 and score<=0.89:
			print('B')
		if score>=0.7 and score<=0.79:	
			print('C')
		if score>=0.6 and score<=0.69:
			print('D')
		if score<0.6:
			print('F')
	else:
		quit()
except:
	print("Bad score!!")
	quit()
	