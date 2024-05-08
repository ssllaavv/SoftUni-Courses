from project.dough import Dough
from project.topping import Topping


class Pizza:
    def __init__(self, name: str, dough: Dough, toppings_capacity: int):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = dict()

    @staticmethod
    def __validate_name(value):
        if value == "":
            raise ValueError("The name cannot be an empty string")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @staticmethod
    def __validate_dough(value):
        if not value:
            raise ValueError("You should add dough to the pizza")

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        self.__validate_dough(value)
        self.__dough = value

    @staticmethod
    def __validate_toppings_capacity(value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        
    @property
    def toppings_capacity(self):
        return self.__toppings_capacity
    
    @toppings_capacity.setter
    def toppings_capacity(self, value):
        self.__validate_toppings_capacity(value)
        self.__toppings_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) < self.toppings_capacity:
            topping_type = topping.topping_type
            if topping_type not in self.toppings.keys():
                self.toppings[topping_type] = 0
            self.toppings[topping_type] += topping.weight

        else:
            raise ValueError("Not enough space for another topping")

    def calculate_total_weight(self):
        total_weight = self.dough.weight + sum(self.toppings.values())
        return total_weight
