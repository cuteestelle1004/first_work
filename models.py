# # from django.db import models
# # # A WEBSITE WHERE USERS CAN ORDER FOOD
# # class Food:
# #     price
# #     description
# #     images
# #     name
# # class Car:
# #     my_car = Car()
# #      wheels = 4 
# #     def __init__(self, make, model):
# #         self.make = make  # Instance attribute
# #         self.model = model  # Instance attribute
# class Car:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model
#         self.get_wheels =.get_wheels(cls)| (() -> get_wheels )


#     def display_info(self):
#         print(f"Car make: {self.make}, Model: {self.model}")
#         class Car:
#          wheels = 4  # Class attribute

#     def get_wheels(cls):
#         return cls.wheels
    
# class Car:

#     def honk():
#         print("Honk! Honk!")
#         my_car = Car("Toyota", "Camry")
#         my_car.display_info()  # Output: Car make: Toyota, Model: Camry


# print(Car.get_wheels())  # Output: 4
# Car.honk()  # Output: Honk! Honk!

class Car:
    wheels = 4  # Class attribute

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Car make: {self.make}, Model: {self.model}")

    @classmethod
    def get_wheels(cls):
        return cls.wheels

    @staticmethod
    def honk():
        print("Honk! Honk!")


# Create an instance of Car
my_car = Car("Toyota", "Camry")

# Display car info
my_car.display_info()  # Output: Car make: Toyota, Model: Camry

# Call class method
print(Car.get_wheels())  # Output: 4

# Call static method
Car.honk()  # Output: Honk! Honk!
Car.__prepare__()






