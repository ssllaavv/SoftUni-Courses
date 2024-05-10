from project.animals.animal import Animal, Mammal
from project.food import Food
from abc import ABC, abstractmethod


class Mouse(Mammal):
    sound = "Squeak"
    foods = ["Vegetable", "Fruit"]
    weight_increase = 0.10

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


class Dog(Mammal):
    sound = "Woof!"
    foods = ["Meat"]
    weight_increase = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


class Cat(Mammal):
    sound = "Meow"
    foods = ["Vegetable", "Meat"]
    weight_increase = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


class Tiger(Mammal):
    sound = "ROAR!!!"
    foods = ["Meat"]
    weight_increase = 1.0

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)


