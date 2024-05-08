from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def _find_worker_by_name(self, worker_name):
        worker = None
        for w in self.workers:
            if w.name == worker_name:
                worker = w
                break
        return worker

    def add_animal(self, animal: Animal, price):
        if self.__animal_capacity > len(self.animals):
            if self.__budget - price >= 0:
                self.__budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {animal.__class__.__name__} added to the zoo"
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        worker = self._find_worker_by_name(worker_name)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        needed_money = sum(w.salary for w in self.workers)
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        needed_money = sum(a.money_for_care for a in self.animals)
        if self.__budget >= needed_money:
            self.__budget -= needed_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals\n----- {len(lions)} Lions:\n"

        for lion in lions:
            result += f"{lion}\n"

        result += f"----- {len(tigers)} Tigers:\n"

        for tiger in tigers:
            result += f"{tiger}\n"

        result += f"----- {len(tigers)} Cheetahs:"

        for cheetah in cheetahs:
            result += f"\n{cheetah}"

        return result

    def workers_status(self):
        vets = [v for v in self.workers if v.__class__.__name__ == "Vet"]
        keepers = [k for k in self.workers if k.__class__.__name__ == "Keeper"]
        caretakers = [c for c in self.workers if c.__class__.__name__ == "Caretaker"]

        result = f"You have {len(self.workers)} workers\n----- {len(keepers)} Keepers:\n"

        for keeper in keepers:
            result += f"{keeper}\n"

        result += f"----- {len(caretakers)} Caretakers:\n"

        for caretaker in caretakers:
            result += f"{caretaker}\n"

        result += f"----- {len(vets)} Vets:"

        for vet in vets:
            result += f"\n{vet}"

        return result








