def fibonacci(num):
    a0 = 0
    a1 = 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    k = 1
    index = 0
    while k < num and num > 1:
        temp = a0
        a0 = a1
        a1 = temp + a0
        k += 1
        if k == num - 1:
            index += num
    return a1
count = 0
n = 1
first_1000_digit = 0
while count < n:
    if len(str(fibonacci(count))) == 1000:
        first_1000_digit += count
        break
    else:
        n += 1
    count += 1
print(first_1000_digit)