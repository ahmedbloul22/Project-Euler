from math import sqrt
word = str(input("Enter a word: "))
def convenable(item):
    numbers = []
    for b in range(0, 9 + 1):
        numbers.append(str(b))
    for c in range(0, 9 + 1):
        if item.find(numbers[c]) != -1:
            return False
    if item != item.lower():
        return False
    return True

slice1 = ""
slice2 = ""
for i in range(1, int(len(word) / 2) + 1):
    slice1 = slice1 + word[-i]
for j in range(0, int(len(word) / 2)):
        slice2 = slice2 + word[j]
if convenable(word):
    if slice1 == slice2:
        print(f"{word} is palindrome")
    else:
        print(f"{word} is not palindrome")
else:
    print("Le mot doit être érit en lettres alaphabétiques et ne doit pas contenir des chiffres.")