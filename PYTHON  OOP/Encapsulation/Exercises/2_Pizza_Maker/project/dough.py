class Dough:
    def __init__(self, flour_type: str, baking_technique: str, weight: float):
        self.flour_type = flour_type
        self.baking_technique = baking_technique
        self.weight = weight

    @staticmethod
    def __validate_floor_type(value):
        if value == "":
            raise ValueError("The flour type cannot be an empty string")

    @property
    def flour_type(self):
        return self.__flour_type

    @flour_type.setter
    def flour_type(self, value):
        self.__validate_floor_type(value)
        self.__flour_type = value

    @staticmethod
    def __validate_baking_technique(value):
        if value == "":
            raise ValueError("The baking technique cannot be an empty string")

    @property
    def baking_technique(self):
        return self.__baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        self.__validate_baking_technique(value)
        self.__baking_technique = value

    @staticmethod
    def __validate_weight(value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__validate_weight(value)
        self.__weight = value




