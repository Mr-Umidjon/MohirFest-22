class Class1:
    num = 15


print(Class1)
print(100 * '-')

object1 = Class1()
print(object1.num)
print(100 * '-')


class Auto:
    def __init__(self, model, name, year, price):
        self.model = model
        self.name = name
        self.year = year
        self.price = price

    def __str__(self):
        return 'Auto class'


spark = Auto("Daewoo", 'Spark', 2006, 2000)
print(spark.price, spark.year)
print(100 * '-')

print(spark)
print(100 * '-')
