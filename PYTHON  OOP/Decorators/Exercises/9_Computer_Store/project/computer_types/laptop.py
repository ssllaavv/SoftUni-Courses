from project.computer_types.computer import Computer


class Laptop(Computer):
    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200,
    }

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{ processor } is not compatible with laptop "
                             f"{ self.manufacturer } { self.model }!")
        if ram not in self.AVAILABLE_RAMS or ram == 128:
            raise ValueError(f"{ ram }GB RAM is not compatible with laptop "
                             f"{ self.manufacturer } { self.model }!")

        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_PROCESSORS[processor] + self.AVAILABLE_RAMS[ram]

        return f"Created {self.manufacturer} {self.model} " \
               f"with {processor} and {ram}GB RAM for {self.price}$."






