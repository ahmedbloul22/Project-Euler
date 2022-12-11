def factorial(n):
    if n == 0:
        return 1
    a = 1
    for b in range(1, n + 1):
        a *= b
    return a
sum = 0
k = 0
while 10**k < factorial(100):
    k += 1
    sum += int((factorial(100) % 10 ** k) / 10 ** (k - 1))
print(sum)
