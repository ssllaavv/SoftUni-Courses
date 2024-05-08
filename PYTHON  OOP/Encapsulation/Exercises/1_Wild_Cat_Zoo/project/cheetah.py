from project.animal import Animal


class Cheetah(Animal):
    def __init__(self, name, gender, age, money_for_care=60):
        super().__init__(name, gender, age, money_for_care)

    @property
    def money_for_care(self):
       return self.__money_for_care

    @money_for_care.setter
    def money_for_care(self, value):
        self.__money_for_care = 60

