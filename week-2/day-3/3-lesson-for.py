numbers = [1, 2, 3, 4, 5, 6, 5, 7, 3, 9]
text = "computer"

for t in text:
    print(t)
print(100 * '-')

for num in numbers:
    print(num)
print(100 * '-')

for num in numbers:
    if num % 2 == 0:
        print(num)
print(100 * '-')

for num in numbers:
    if num % 2 == 1:
        print(num)
print(100 * '-')
