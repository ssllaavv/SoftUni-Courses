from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):

    sound = ""
    foods = []
    weight_increase = 0

    @abstractmethod
    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @classmethod
    def make_sound(cls):
        return cls.sound

    def feed(self, food: Food):
        if food.__class__.__name__ in self.foods:
            self.food_eaten += food.quantity
            self.weight += self.weight_increase * food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


class Mammal(Animal, ABC):

    @abstractmethod
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Bird(Animal, ABC):

    @abstractmethod
    def __init__(self, name, weight,  wing_size):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

