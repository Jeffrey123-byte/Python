# class Test:
#     x = 10  # class attribute

#     def __init__(self):
#         self.x = 20  # instance attribute

# obj = Test()
# print(obj.x)  # Outputs 20, not 10

class A:
    goal = "Learn Python"

obj = A()
print(obj.goal)

obj.goal = "Master Python"
print(obj.goal)
print(A.goal)

