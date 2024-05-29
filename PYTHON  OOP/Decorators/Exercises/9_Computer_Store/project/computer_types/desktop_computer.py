from project.computer_types.computer import Computer


class DesktopComputer(Computer):

    AVAILABLE_PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800,
    }

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.AVAILABLE_PROCESSORS:
            raise ValueError(f"{ processor } is not compatible with desktop computer"
                             f" {self.manufacturer } { self.model }!")
        if ram not in self.AVAILABLE_RAMS:
            raise ValueError(f"{ ram }GB RAM is not compatible with desktop computer"
                             f" { self.manufacturer } { self.model }!")

        self.processor = processor
        self.ram = ram
        self.price += self.AVAILABLE_PROCESSORS[processor] + self.AVAILABLE_RAMS[ram]

        return f"Created { self.manufacturer } { self.model } " \
               f"with { processor } and { ram }GB RAM for { self.price }$."





