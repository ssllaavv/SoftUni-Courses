from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    def _find_dvd_by_id(self, id):
        dvd = None
        for d in self.dvds:
            if d.id == id:
                dvd = d
                break
        return dvd

    def _find_customer_by_id(self, id):
        customer = None
        for c in self.customers:
            if c.id == id:
                customer = c
                break
        return customer

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_customer_by_id(customer_id)
        dvd = self._find_dvd_by_id(dvd_id)
        if customer and dvd:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            elif dvd.is_rented:
                return "DVD is already rented"
            elif customer.age < dvd.age_restriction:
                return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
            else:
                dvd.is_rented = True
                customer.rented_dvds.append(dvd)
                return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self._find_customer_by_id(customer_id)
        dvd = self._find_dvd_by_id(dvd_id)
        if customer and dvd:
            if dvd in customer.rented_dvds and dvd.is_rented:
                customer.rented_dvds.remove(dvd)
                dvd.is_rented = False
                return f"{customer.name} has successfully returned {dvd.name}"
        return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = ""
        for c in self.customers:
            result += f"{c}\n"
        for d in self.dvds:
            result += f"{d}\n"

        result = result[:-1:]
        return result




