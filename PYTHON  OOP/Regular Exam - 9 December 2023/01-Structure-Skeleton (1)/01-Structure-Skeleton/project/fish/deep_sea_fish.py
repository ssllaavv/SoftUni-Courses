from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    def __init__(self, name, points):
        super().__init__(name, points, time_to_catch=180)
        self.time_to_catch = 180

    def fish_details(self):
        return f"{self.__class__.__name__}: {self.name} [Points: {self.points}, " \
               f"Time to Catch: {self.time_to_catch} seconds]"



