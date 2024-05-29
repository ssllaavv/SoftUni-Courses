from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in ["Desktop Computer", "Laptop"]:
            raise ValueError(f"{ type_computer } is not a valid type computer!")

        result = None
        if type_computer == "Desktop Computer":
            computer = DesktopComputer(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
            result = computer.configure_computer(processor, ram)
            self.warehouse.append(computer)

        return result


    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        computer = None
        for c in self.warehouse:
            if all([c.processor == wanted_processor, c.ram >= wanted_ram, c.price <= client_budget]):
                computer = c
                break
        if computer:
            self.warehouse.remove(computer)
            self.profits += client_budget - computer.price
            return f"{ computer } sold for { client_budget }$."
        raise Exception("Sorry, we don't have a computer for you.")
