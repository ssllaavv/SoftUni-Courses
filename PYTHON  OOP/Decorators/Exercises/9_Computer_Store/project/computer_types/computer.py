from abc import ABC, abstractmethod


class Computer(ABC):

    AVAILABLE_PROCESSORS = {}
    AVAILABLE_RAMS = {
        2: 100,
        4: 200,
        8: 300,
        16: 400,
        32: 500,
        64: 600,
        128: 700,
    }

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price = 0
        
    @property
    def manufacturer(self):
        return self.__manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        if value.strip() == '':
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if value.strip() == '':
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        ...

    def __repr__(self):
        return f"{ self.manufacturer } { self.model } with { self.processor } and { self.ram }GB RAM"



