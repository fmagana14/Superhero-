class Animal:
    def __init__(self, name, ):
        self.name = name

    def eat(self):
            print(f"{self.name} is eating.")
    
    def drink(self):
         print(f"{self.name} id drinking water.")

class frog(Animal):
     def jump(self):
          print(f"{self.name} jumps high!")

frog = frog("Roger")
frog.eat()
frog.drink()
frog.jump()