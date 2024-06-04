from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.main_dish import MainDish
from project.meals.dessert import Dessert
from project.client import Client


class FoodOrdersApp:
    def __init__(self):
        self.clients_list = []
        self.menu = []
        self.receipt_id = 1

    def _find_client_by_phone_number(self, phone_number):
        client = None
        for c in self.clients_list:
            if c.phone_number == phone_number:
                client = c
                break
        return client

    def _find_meal_by_name(self, name):
        meal = None
        for m in self.menu:
            if m.name == name:
                meal = m
                break
        return meal

    def register_client(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")
        client = Client(client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in ["Starter", "MainDish", "Dessert" ]:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        result = []
        for meal in self.menu:
            result.append(meal.details())
        return '\n'.join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        client = self._find_client_by_phone_number(client_phone_number)
        if not client:
            self.register_client(client_phone_number)
            client = self._find_client_by_phone_number(client_phone_number)

        absent_meal = None
        for m_name in meal_names_and_quantities.keys():
            meal = self._find_meal_by_name(m_name)
            if not meal:
                absent_meal = m_name
                break
        if absent_meal:
            raise Exception(f"{absent_meal} is not on the menu!")

        absent_meal = None
        meal = None
        for m_name, qtt in meal_names_and_quantities.items():
            meal = self._find_meal_by_name(m_name)
            if meal.quantity < qtt:
                absent_meal = m_name
                break
        if absent_meal:
            raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {absent_meal}!")

        for m_name, qtt in meal_names_and_quantities.items():
            meal = self._find_meal_by_name(m_name)
            client.shopping_cart.append(meal)
            client.bill += meal.price * qtt
            meal.quantity -= qtt

        client.ordered_meal_names_and_quantities.extend(meal_names_and_quantities.items())

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join([m[0] for m in client.ordered_meal_names_and_quantities])} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")
        for meal in client.shopping_cart:
            self.menu[meal.quantity] += client.ordered_meal_names_and_quantities[meal.name]
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meal_names_and_quantities = []

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_phone_number(client_phone_number)
        if len(client.shopping_cart) == 0:
            raise Exception("There are no ordered meals!")

        result = f"Receipt #{self.receipt_id} with total amount of " \
                 f"{client.bill:.2f} was successfully paid for {client.phone_number}."
        self.receipt_id += 1
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meal_names_and_quantities = []
        return result

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} " \
               f"meals on the menu and {len(self.clients_list)} clients."
