class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print("Barking...")


dog1 = Dog("buddy",23)
print(dog1.name)
print(dog1.age)
dog1.bark()