from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age, gender="female"):
        super().__init__(name, age, gender="female")
        self.gender = "Female"

    def make_sound(self):
        return "Meow"


