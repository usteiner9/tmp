# import collections
from collections import namedtuple

tup = ('hello', object(), 42)
print(tup)
print(tup[2])


# up comes NamedTuples

Car = namedtuple('Car', 'color mileage')


my_car = Car('red', 3812.4)

print(my_car.color)

print(my_car.mileage)

print(my_car[0])

print(my_car[1])

print(tuple(my_car))

color, mileage = my_car

print(color, mileage)

print(*my_car)

print(my_car)

# up comes Subclassing Namedtuples

Car = namedtuple('Car', 'color mileage')


class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

c = MyCarWithMethods('red', 1234)
print(c.hexcolor)

Car = namedtuple('Car', 'color mileage')
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
print(ElectricCar('red', 1234, 45.0))
