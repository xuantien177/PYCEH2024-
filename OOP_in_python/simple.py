class Car:
    def __init__(self, make_and_model, year, gearbox):
        self.make_and_model = make_and_model
        self.year = year
        self.gearbox = gearbox

    def drive(self):
        print(f"{self.make_and_model}, {self.year}, {self.gearbox} is NOW DRIVING")
    
    def stop(self):
        print(f"{self.make_and_model}, {self.year}, {self.gearbox} is STOPPED")

# Lớp ElectricCar kế thừa từ Car
class ElectricCar(Car):
    def charge(self):
        print(f"{self.make_and_model} is now charging.")

# Sử dụng lớp ElectricCar
my_electric_car = ElectricCar("Tesla Model S", 2020, "Automatic")
my_electric_car.drive()
my_electric_car.charge()
my_electric_car.stop()



class Pet:
    def __init__(self, type, name, age, color):
        self.type = type
        self.name = name
        self.age = age
        self.color = color
    
    def play(self):
        print(f"\nThis is {self.type} named {self.name} with {self.color} color and {self.age} years old is PLAYING")

    def sleep(self):
        print(f"\nThis is {self.type} named {self.name} with {self.color} color tired,so it is SLEEPING")

#Class Dog kế thừa từ class Pet đang thực hiện hành động sủa :)))
class Dog(Pet):
    def bark(self):
        print(f"\nThat {self.type} named {self.name}  is BARKING")

#Sử dụng class Dog

pet1=Pet('cat','Miuw','5','black')
dog1=Dog('dog','Huston',6,'orange')
pet1.sleep()
dog1.play()
dog1.bark()
dog1.sleep()


