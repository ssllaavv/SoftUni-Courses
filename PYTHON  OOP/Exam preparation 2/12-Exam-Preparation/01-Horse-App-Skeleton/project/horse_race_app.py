from project.horse_race import HorseRace
from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    HORSES_TYPES = ["Appaloosa", "Thoroughbred"]

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def _find_last_free_horse_of_a_type(self, horse_type: str):
        horse = None
        for h in reversed(self.horses):
            if h.__class__.__name__ == horse_type and not h.is_taken:
                horse = h
                break
        return horse

    def _find_horse_by_name(self, name: str):
        horse = None
        for h in self.horses:
            if h.name == name:
                horse = h
                break
        return horse

    def _find_jockey_by_name(self, name: str):
        jockey = None
        for j in self.jockeys:
            if j.name == name:
                jockey = j
                break
        return jockey

    def _find_race_by_type(self, race_type):
        race = None
        for r in self.horse_races:
            if r.race_type == race_type:
                race = r
                break
        return race

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self._find_horse_by_name(horse_name)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.HORSES_TYPES:
            horse = eval(horse_type)(horse_name, horse_speed)
            self.horses.append(horse)
            return f"{horse_type} horse {horse_name} is added."
    #
    # def add_jockey(self, jockey_name: str, age: int):
    #     jockey = self._find_jockey_by_name(jockey_name)
    #     if jockey:
    #         raise Exception(f"Jockey {jockey_name} has been already added!")
    #
    #     jockey = Jockey(jockey_name, age)
    #     self.jockeys.append(jockey)
    #     return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = self._find_race_by_type(race_type)
        if race:
            raise Exception("Race {race type} has been already created!")

        race = HorseRace(race_type)
        self.horse_races.append(race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._find_jockey_by_name(jockey_name)
        horse = self._find_last_free_horse_of_a_type(horse_type)

        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not horse:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse:
            return f"Jockey {jockey_name} already has a horse."

        horse.is_taken = True
        jockey.horse = horse
        return f"Jockey {jockey_name} will ride the horse {horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self._find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        jockey = self._find_jockey_by_name(jockey_name)
        if not jockey:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if not jockey.horse:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        race = self._find_race_by_type(race_type)
        if not race:
            raise Exception(f"Race {race_type} could not be found!")

        if len(race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = race.jockeys[0]
        for j in race.jockeys:
            if j.horse.speed > winner.horse.speed:
                winner = j

        return f"The winner of the {race_type} race, with a speed of " \
               f"{winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}."



