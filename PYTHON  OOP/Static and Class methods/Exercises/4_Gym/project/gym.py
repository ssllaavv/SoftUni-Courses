from project.customer import Customer
from project.trainer import Trainer
from project.exercise_plan import ExercisePlan
from project.equipment import Equipment
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def _find_subscription_by_id(self, id):
        subscription = None
        for s in self.subscriptions:
            if s.id == id:
                subscription = s
                break
        return subscription

    def _find_customer_by_id(self, id):
        customer = None
        for c in self.customers:
            if c.id == id:
                customer = c
                break
        return customer

    def _find_trainer_by_id(self, id):
        trainer = None
        for t in self.trainers:
            if t.id == id:
                trainer = t
                break
        return trainer

    def _find_equipment_by_id(self, id):
        equipment = None
        for e in self.equipment:
            if e.id == id:
                equipment = e
                break
        return equipment

    def _find_plan_by_id(self, id):
        plan = None
        for p in self.plans:
            if p.id == id:
                plan = p
                break
        return plan

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self._find_subscription_by_id(subscription_id)
        if subscription:
            customer = self._find_customer_by_id(subscription.customer_id)
            trainer = self._find_trainer_by_id(subscription.customer_id)
            plan = self._find_plan_by_id(subscription.exercise_id)
            equipment = self._find_equipment_by_id(plan.equipment_id)

            result = str(subscription) + "\n" + str(customer) + "\n" + str(trainer) + "\n"\
                     + str(equipment) + "\n" + str(plan)

            return result



