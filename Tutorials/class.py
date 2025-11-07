class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.make} {self.model} is driving.")

    def stop(self):
        print(f"The {self.make} {self.model} has stopped.")

my_car = Car("Toyota", "Corolla", "blue")
your_car = Car("Honda", "Civic", "red")

my_car.drive()
your_car.stop()
