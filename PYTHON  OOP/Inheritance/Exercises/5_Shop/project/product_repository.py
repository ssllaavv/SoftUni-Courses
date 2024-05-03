from project.food import Food
from project.drink import Drink
from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name):
        product = None
        for p in self.products:
            if p.name == product_name:
                product = p
                return product

    def remove(self, product_name):
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self):
        result = ""
        for p in self.products:
            result += f"{p.name}: {p.quantity}\n"
        result = result[:-1:]
        return result
