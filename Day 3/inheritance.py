class Worker : 
    def __init__(self,name,address,hourly_salary):
        self.name = name
        self.address = address
        self.hourly_salary = hourly_salary

    def show_profile(self):
        print('============ Work Proile =============')
        print(f"Name : {self.name}")
        print(f"Address : {self.address}")
        print(f"Hourly salary: {self.hourly_salary}")

    def calculate_payroll(self, hours = 40):
        return self.hourly_salary*hours
    
class Manager(Worker):
    def __init__(self,name,address,hourly_salary, hourly_bonus):
        super().__init__(name,address,hourly_salary)
        self.hourly_bonus=hourly_bonus

    def calculate_payroll(self, hours=40):
        return(self.hourly_salary + self.hourly_bonus) * hours
    
    def show_profile(self):
        super().show_profile()
        print(f"Hourly bonus: {self.hourly_bonus}")

worker1 = Worker("Janice", "124 main street", 35)
manager1 = Manager("Bob", "456 elm street" , 24 , 5)

worker1.show_profile()
manager1.show_profile()

manager1.calculate_payroll(50)
print(f"Manages payroll for 50 hours: {manager1.calculate_payroll(50)}")

