#attributes and vaiables methods objects 
# poperties attributes methods
# class attributes and instance attributes
#constuctos and destructors getter and settes

class Person:
    goal = 'to learn Python'  # class attribute
    def __init__(self,name,age):
        self.name = name
        self.age = age #instance attributes

    def get_name(self):  #getter method
        return self.name
        return self.age
    def set_name(self, name,age): #setter method
        self.name = name    
        self.age = age

    def print_info(self):
        print(f'Name: {self.name}, Age: {self.age}, Goal: {self.goal}') 

Person1 = Person('Alice', 30)
Person1.print_info()# non updated goal
updated_goal = 'to master Python programming'

Person.goal = updated_goal # updating class attribute
Person1.print_info()
    
