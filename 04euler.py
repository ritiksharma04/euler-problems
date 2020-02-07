#to check pallindrome

for i in range(999,900,-1):
	for j in range(999,900,-1):
		a = i*j
		temp = str(a)
		if(temp[::-1]== temp):
			print(a)

