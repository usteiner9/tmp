class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f'a {self.color} car'

my_car = Car('red', 37281)
print(my_car)
my_car
print(str(my_car))
'{}'.format(my_car)

