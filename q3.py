class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Cat names {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")

ella = Cat("Ella")
ella.speak()

class Dog:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f"a Dog's name is {self.name}"

bob = Dog("buddy")
print(bob)