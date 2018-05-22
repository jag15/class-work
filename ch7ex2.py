fname=input('Enter the file name: ')
fhand=open(fname)
count=0
total=0.0
for line in fhand:
	if line.startswith('X-DSPAM-Confidence:'):	
		sline=float(line[20:])
		total=total+sline
		count=count+1
print('Average Spam Confidence: ', total/count)
