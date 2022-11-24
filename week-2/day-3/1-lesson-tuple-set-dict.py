fruits = ('apple', 'banana', 'cherry')

print(fruits)
print(100 * "-")

print(fruits[0])
print(100 * "-")

print(len(fruits))
print(100 * "-")

print(type(fruits))
print(100 * "-")

boolean = (True, False, True)

print(boolean)
print(100 * "-")

for fruit in fruits:
    print(fruit)
print(100 * "-")

set_num = {1, 3, 2, 1, 4, 4, 3}
print(set_num)
print(100 * "-")

set_num = {1, 3, 2, 1, 4, 4, 3}
print(len(set_num))
print(100 * "-")

set_num = {1, 3, 2, 1, 4, 4, 3}
print(type(set_num))
print(100 * "-")

set_num.add(23)
print(set_num)
print(100 * "-")

set_num.update([6, 5, 7])
print(set_num)
print(100 * "-")

set_num.remove(1)
print(set_num)
print(100 * "-")

for num in set_num:
    print(num)
print(100 * "-")

set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3, 4}
set3 = set1.union(set2)
print(set3)
print(100 * "-")
