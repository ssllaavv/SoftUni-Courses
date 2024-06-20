class Animal:

    SPECIES_SOUNDS = {"cat": "meow", "dog": "woof-woof", "chicken": "chick"}

    def __init__(self, species, sound=None):
        self.species = species
        if species not in Animal.SPECIES_SOUNDS.keys():
            Animal.SPECIES_SOUNDS[species] = sound

    def get_species(self):
        return self.species

    def make_sound(self):
        return Animal.SPECIES_SOUNDS[self.species]


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


tiger = Animal("tiger")

animals = [Animal('cat'), Animal('dog'), Animal('chicken'), tiger]
animal_sound(animals)

print(Animal.SPECIES_SOUNDS)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
