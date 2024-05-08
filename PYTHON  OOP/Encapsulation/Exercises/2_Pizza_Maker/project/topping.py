class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight

    @staticmethod
    def __validate_topping_type(value):
        if value == "":
            raise ValueError("The topping type cannot be an empty string")

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value):
        self.__validate_topping_type(value)
        self.__topping_type = value

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

