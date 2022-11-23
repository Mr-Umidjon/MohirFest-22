fruits = ['apple', 'cherry', 'orange']

print(fruits[0])
print(100*'-')

print(fruits[-1])
print(100*'-')

print(fruits[0:2])
print(100*'-')

fruits[1] = 'banana'
print(fruits)
print(100*'-')

fruits.append('cherry')
print(fruits)
print(100*'-')

fruits.insert(1, 'cherry')
print(fruits)
print(100*'-')

number = [1, 2, 3, 4]
fruits.extend(number)
print(fruits)
print(100*'-')

fruits.remove(1)
print(fruits)
print(100*'-')

fruits.pop()
print(fruits)
print(100*'-')

fruits.pop(-2)
print(fruits)
print(100*'-')

del fruits[-1]
print(fruits)
print(100*'-')

fruits.clear()
print(fruits)
print(100*'-')
