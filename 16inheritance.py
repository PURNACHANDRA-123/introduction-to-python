class vehicle:
    def general_info(self):
        print("general use =transportation")

class car(vehicle):
    def __init__(self):
        print("iam a car")
        self.wheel=4
        self.has_roof=True
    def specific_info(self):
        
        print("better for family trips")


class bike(vehicle):
    def __init__(self):
        print("iam a bike")
        self.wheel=2
        self.has_roof=False
    def specific_info(self):
        
        print("better for road trips")

c=car()
c.general_info()
c.specific_info()


b=bike()
b.general_info()
b.specific_info()

print(isinstance(c,car))
#tells whether c is an instance/belongs to of car or not
print(isinstance(b,car))
#here you will get false bcoz b is not an instance/belongs of car

print(issubclass(car,vehicle))
#tells whether car is a subclass of vehicle or not
print(issubclass(bike,car))
#here you will get false bcoz bike is not a subclass of car







