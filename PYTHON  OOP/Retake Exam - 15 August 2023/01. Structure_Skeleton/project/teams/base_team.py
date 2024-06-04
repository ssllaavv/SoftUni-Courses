from abc import ABC, abstractmethod
from math import floor


class BaseTeam(ABC):
    def __init__(self, name: str, country: str, advantage: int, budget: float):
        self.name = name
        self.country = country
        self.advantage = advantage
        self.budget = budget
        self.wins = 0
        self.equipment = []
        
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Team name cannot be empty!")
        self.__name = value 
        
    @property
    def country(self):
        return self.__country
    
    @country.setter
    def country(self, value):
        if len(value.strip()) < 2:
            raise ValueError("Team country should be at least 2 symbols long!")
        self.__country = value

    @property
    def advantage(self):
        return self.__advantage

    @advantage.setter
    def advantage(self, value):
        if value <= 0:
            raise ValueError("Advantage must be greater than zero!")
        self.__advantage = value

    @abstractmethod
    def win(self):
        ...

    def get_statistics(self):

        equipment_count = len(self.equipment)
        if equipment_count == 0:
            equipment_count = 1

        return f"Name: {self.name}" \
               f"\nCountry: {self.country}" \
               f"\nAdvantage: {self.advantage} points" \
               f"\nBudget: {self.budget:.2f}EUR" \
               f"\nWins: {self.wins}" \
               f"\nTotal Equipment Price: {sum([e.price for e in self.equipment ]):.2f}" \
               f"\nAverage Protection: {floor(sum([e.protection for e in self.equipment]) / equipment_count)}"









