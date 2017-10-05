class Car():
    no_of_wheels =4
    
    def __init__(self,color,make,year):
        self.color = color
        self.make = make
        self.year = year

    def drive(self,acceleration):
        print('you cant this car yet')

my_car = Car('white','toyota',2012)
print (my_car.no_of_wheels)
print (my_car.color)
my_second_car = Car("green","volvo",1926)

my_car.no_of_wheels= 12
my_second_car.no_of_wheels= 24
print (my_car.no_of_wheels)


