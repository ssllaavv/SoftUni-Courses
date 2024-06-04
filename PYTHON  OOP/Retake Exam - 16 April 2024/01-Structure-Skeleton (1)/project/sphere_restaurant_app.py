from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    def __init__(self):
        self.waiters = []
        self.clients = []

    def _find_waiter_by_name(self, name):
        waiter = None
        for w in self.waiters:
            if w.name == name:
                waiter = w
                break
        return waiter

    def _find_client_by_name(self, name):
        client = None
        for c in self.clients:
            if c.name == name:
                client = c
                break
        return client

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):

        waiter_types = ["FullTimeWaiter", "HalfTimeWaiter"]
        if waiter_type not in waiter_types:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = self._find_waiter_by_name(waiter_name)
        if waiter :
            return f"{waiter_name} is already on the staff."

        waiter = eval(waiter_type)(waiter_name, hours_worked)
        self.waiters.append(waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):

        clients_types = ["RegularClient", "VIPClient"]
        if client_type not in clients_types:
            return f"{client_type} is not a recognized client type."

        client = self._find_client_by_name(client_name)
        if client:
            return f"{client_name} is already a client."

        client = eval(client_type)(client_name)
        self.clients.append(client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self._find_waiter_by_name(waiter_name)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."
        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self._find_client_by_name(client_name)
        if not client:
            return f"{client_name} is not a registered client."

        return f"{client_name} earned {client.earning_points(order_amount)} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self._find_client_by_name(client_name)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):

        total_earnings = 0
        for w in self.waiters:
            total_earnings += w.calculate_earnings()

        total_client_points = 0
        for c in self.clients:
            total_client_points += c.points

        # waiters_and_earnings = [(w.name, w.calculate_earnings) for w in self.waiters]

        sorted_waiters = sorted(self.waiters, key=lambda x: x.calculate_earnings(), reverse=True)

        result = f"$$ Monthly Report $$\nTotal Earnings: ${total_earnings:.2f}\n" \
                 f"Total Clients Unused Points: {total_client_points}\n" \
                 f"Total Clients Count: {len(self.clients)}\n** Waiter Details **"

        for w in sorted_waiters:
            result += f"\n{str(w)}"

        return result













