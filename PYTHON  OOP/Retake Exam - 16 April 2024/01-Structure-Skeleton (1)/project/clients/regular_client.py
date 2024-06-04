from math import floor


from project.clients.base_client import BaseClient


class RegularClient(BaseClient):
    def __init__(self, name: str):
        super().__init__(name, membership_type="Regular")

    def earning_points(self, order_amount: float):
        points = floor(order_amount * .1)
        self.points += points
        return points

