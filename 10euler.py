# sum of primes under 2 million

prime = [True for i in range(2000000)]

#seive of eratosthenes
for curr_prime in range(2, 2000000):
    if prime[curr_prime]:
        for i in range(curr_prime*2, 2000000, curr_prime):
            prime[i] = False

sum = 0
for i in range(2, 2000000):
    if prime[i]:
        sum += i
print(sum)