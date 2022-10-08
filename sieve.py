N = 100000
prime = [True for i in range(N + 1)]
p = 2
while (p * p <= N):
    if (prime[p]):
        for i in range(p * p, N + 1, p):
            prime[i] = False
    p += 1
prime[1] = False
inp = int(input("Enter a number less than 100000: "))
if (prime[inp]):
    print("The number is prime")
else:
    print("The number is not prime")
