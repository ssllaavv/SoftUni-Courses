class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0
        self.ordered_meal_names_and_quantities = []

    @property
    def phone_number(self):
        return self.__phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        value_list = list(value)
        if value_list[0] != "0" or len(value_list) != 10 or not all(v.isdigit() for v in value_list):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value
