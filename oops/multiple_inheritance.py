# multiple inheritance = inherit from more than one parent class
# i.e.   C(A, b)

# multilevel inheritance = inherit from a parent which inherits from another parent
# i.e.   C(B) <- B(A) <- A

class Animal:
    def __init__(self,name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing.")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting.")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit=Rabbit("Tony")
hawk=Hawk("Rocket")
fish=Fish("Nemo")

rabbit.flee()
fish.hunt()
fish.flee()

rabbit.eat()
rabbit.sleep()