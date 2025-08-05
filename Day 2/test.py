class person:
    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email =email
    def get_info(self):
        return self.name,self.age,self.email
        
    def set_info(self,name ,age, email):
        self.name = name
        self.age = age
        self.email =email

    def printing(self):
        print(f'His name is {self.name} his age is  {self.age} and his email is {self.email}')

obj = person("Rey", 23,"jeffreyjebastin@gmail.com")
obj.printing() 
print(obj.name)
