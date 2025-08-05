class Secret:
    globe =  "Global variable"
    def __init__(self):
        self.public = "I am public"
        self.__private = "I am private"
        self.private = "I am the real private"

    # def show(self):
    #     print('Public : ', self.public)
    #     print('Private : ', self.__private)
    #     print('Real Private : ', self.private)

obj = Secret()
update_globe = " Global variable has become complete "
obj.globe = update_globe
# obj.show()

print(obj.public)  # Accessing public variable
print(obj.private)
print(obj._Secret__private) 
print(obj.globe)
# # Accessing public variable
# print(obj.public)

# # Trying to access private directly (will fail)
# # print(obj.__private)  # ❌ This will raise AttributeError

# # Correct way using name mangling
# print(obj._Secret__private)  # ✅ Works!
