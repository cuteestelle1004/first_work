# # # # from django.db import models
# # # # # A WEBSITE WHERE USERS CAN ORDER FOOD
# # # # class Food:
# # # #     price
# # # #     description
# # # #     images
# # # #     name
# # # # class Car:
# # # #     my_car = Car()
# # # #      wheels = 4 
# # # #     def __init__(self, make, model):
# # # #         self.make = make  # Instance attribute
# # # #         self.model = model  # Instance attribute
# # # class Car:
# # #     def __init__(self, make, model):
# # #         self.make = make
# # #         self.model = model
# # #         self.get_wheels =.get_wheels(cls)| (() -> get_wheels )


# # #     def display_info(self):
# # #         print(f"Car make: {self.make}, Model: {self.model}")
# # #         class Car:
# # #          wheels = 4  # Class attribute

# # #     def get_wheels(cls):
# # #         return cls.wheels
    
# # # class Car:

# # #     def honk():
# # #         print("Honk! Honk!")
# # #         my_car = Car("Toyota", "Camry")
# # #         my_car.display_info()  # Output: Car make: Toyota, Model: Camry


# # # print(Car.get_wheels())  # Output: 4
# # # Car.honk()  # Output: Honk! Honk!

# # class Car:
# #     wheels = 4  # Class attribute

# #     def __init__(self, make, model):
# #         self.make = make
# #         self.model = model

# #     def display_info(self):
# #         print(f"Car make: {self.make}, Model: {self.model}")

# #     @classmethod
# #     def get_wheels(cls):
# #         return cls.wheels

# #     @staticmethod
# #     def honk():
# #         print("Honk! Honk!")


# # # # Create an instance of Car
# # # my_car = Car("Toyota", "Camry")

# # # # Display car info
# # # my_car.display_info()  # Output: Car make: Toyota, Model: Camry

# # # # Call class method
# # # print(Car.get_wheels())  # Output: 4

# # # # Call static method
# # # Car.honk()  # Output: Honk! Honk!
# # # Car.__prepare__()


# # class Car:
# #     def __init__(self, color):
# #         self.__color = color

# #     def get_color(self):
# #         return self.__color

# #     def set_color(self, color):
# #         self.__color = color

# class Duck:
#     def quack(self):
#         print("Quack!")

# class Dog:
#     def quack(self):
#         print("Bark like a quack!")

# def make_it_quack(animal):
#     animal.quack()

# make_it_quack(Duck())  # Output: Quack!
# make_it_quack(Dog())   # Output: Bark like a quack!

# student = {"name": "Alice", "age": 21, "grade": "A"}
# print(student["name"])  # Output: Alice

# print(student["age"] == 22)  # Updates age
# student["major"] = "Biology"  # Adds a new key-value pair
# # print(student["major"])

# print(student.pop("grade"))  # Removes "grade" key

# print(student.popitem())

# student.clear()
# "age" in student  # Output: True

# for key in student.keys():
#     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key, value)

# new_data = {"graduated": False, "GPA": 3.8}
# student.update(new_data)

# squares = {x: x ** 2 for x in range(1, 6)}
# print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# from collections import defaultdict
# scores = defaultdict(int)
# scores["Alice"] += 1  # Initializes "Alice" with 0 and then adds 1

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")

try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

try: 
    # Code that may raise an exception
    pass
except Exception as e:
    print("An error occurred:", e)

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Division successful:", result)











