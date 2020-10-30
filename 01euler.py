#sum of multiples of 3 or 5 
n=int(input())
sum=0
for i in range(n):
    if i%3==0 or i%5==0:
        sum+=i
print(sum)
