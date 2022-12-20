from math import sqrt
n = 600851475143
def factors(p):
    factors = []
    crible = int(sqrt(p))
    for i in range(1, crible + 1):
        if p % i == 0:
            factors.append(i)
            factors.append(int(p / i))
    return factors
def isPrime(num):
    if len(factors(num)) == 2:
        return True
    return False
largest_prime = 0
for i in factors(n):
    if isPrime(i) and i > largest_prime:
        largest_prime = i
print(largest_prime)