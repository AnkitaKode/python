class mammal:
    def walk(self):
        print("Walk")


class Dog(mammal):
    def bark(self):
        print("Dog barks.")



dog=Dog()
print(dog.walk())
print(dog.bark())