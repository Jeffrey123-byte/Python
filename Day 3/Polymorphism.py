'''The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
with the same name that can be executed on many objects or classes.'''

# What do you mean by many forms
x = "Hello World!"
print(len(x))

mytuple = ("apple", "banana", "cherry")
print(len(mytuple))

thisdict = {
  "brand": "Lamborghini",
  "model": "Aventador",
  "year": 2012
}
print(len(thisdict))

# WHen it comes to classes they are of two types 

# Method Overiding

class Animal:
    def sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

class Cat(Animal):
    def sound(self):
        print("Meow!")

# Create instances of the classes
animal = Animal()
dog = Dog()
cat = Cat()

# Call the sound() method on each object
animal.sound()  # Output: Generic animal sound
dog.sound()     # Output: Woof!
cat.sound()     # Output: Meow!