from project.animals.animal import Animal, Bird
from project.food import Food
from abc import ABC, abstractmethod


class Owl(Bird):
    def __init__(self, name, weight,  wing_siz):
        super().__init__(name, weight,  wing_siz)

    sound = "Hoot Hoot"
    foods = ["Meat"]
    weight_increase = 0.25


class Hen(Bird):
    def __init__(self, name, weight, wing_siz):
        super().__init__(name, weight, wing_siz)

    sound = "Cluck"
    foods = ["Meat", "Vegetable", "Fruit", "Seed"]
    weight_increase = 0.35







