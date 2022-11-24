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

set1 = {'a', 'b', 'c', 1}
set2 = {1, 2, 3, 4, 'a'}
set3 = set1.union(set2)
print(set3)
print(100 * "-")

set4 = set1.intersection(set2)
print(set4)
print(100 * "-")

me = {
    'name': "Umidbek",
    'age': 20,
    'height': 1.75
}
print(me)
print(100 * "-")

print(len(me))
print(100 * "-")

print(type(me))
print(100 * "-")

print(me['age'])
print(100 * "-")

print(me['name'])
print(100 * "-")

me['age'] = 23
print(me['age'])
print(100 * "-")

me.update({"location": 'Tashkent'})
print(me)
print(100 * "-")

me.pop('age')
print(me)
print(100 * "-")

for item in me:
    print(item)
print(100 * "-")

for key in me.keys():
    print(key)
print(100 * "-")

for value in me.values():
    print(value)
print(100 * "-")

for key, value in me.items():
    print(key, value)
print(100 * "-")
