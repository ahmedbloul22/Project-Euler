
def reversedNumber(num):
    s_num = ""
    for i in reversed(str(num)):
        s_num = s_num + i
    return int(s_num)
largest = 0
for i in range(100, 999 + 1):
    for j in range(100, 999 + 1):
        if i * j == reversedNumber(i * j) and i * j > largest:
            largest = i * j
print(largest)