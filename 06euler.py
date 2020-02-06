sum = 0          #sum of numbers
for i in range(0,101):
	sum = sum +i
b = sum*sum

sq = 0            #sum of square
for j in range(0,101):
	sq = sq + j*j
                  
a = b-sq
print(a)