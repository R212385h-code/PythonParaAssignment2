class Vehicle:
    def move(self):
        print("The vehicle is moving")


class Car(Vehicle):
    def move(self):
        print("The car is driving")


class Bike(Vehicle):
    def move(self):
        print("The bike is riding")


car = Car()
bike = Bike()

car.move()
bike.move()
