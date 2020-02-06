i = 0
n1 = 1
n2 = i + n1
count = 0
sum = 0
while(i<4*10**6):
	if(i %2 == 0):
	    sum = sum + i
	    print(sum)
	nth = i + n1
	i = n1
	n1 = nth
	count += 1

