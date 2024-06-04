from project.fish.base_fish import BaseFish
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.divers.base_diver import BaseFish
from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver


class NauticalCatchChallengeApp:

    DIVERS_TYPES = ["FreeDiver", "ScubaDiver"]
    FISH_TYPES = ["PredatoryFish", "DeepSeaFish"]

    def __init__(self):
        self.divers = []
        self.fish_list = []

    def _find_diver_by_name(self, name: str):
        diver = None
        for d in self.divers:
            if d.name == name:
                diver = d
                break
        return diver

    def _find_fish_by_name(self, name: str):
        fish = None
        for f in self.fish_list:
            if f.name == name:
                fish = f
                break
        return fish

    def dive_into_competition(self, diver_type: str, diver_name: str):

        if diver_type not in self.DIVERS_TYPES:
            return f"{diver_type} is not allowed in our competition."

        diver = self._find_diver_by_name(diver_name)
        if diver:
            return f"{diver_name} is already a participant."

        diver = eval(diver_type)(diver_name)
        self.divers.append(diver)

        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.FISH_TYPES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._find_fish_by_name(fish_name)
        if fish:
            return f"{fish_name} is already permitted."

        fish = eval(fish_type)(fish_name, points)
        self.fish_list.append(fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._find_diver_by_name(diver_name)
        fish = self._find_fish_by_name(fish_name)

        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                if diver.oxygen_level == 0:
                    diver.has_health_issue = True
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            if diver.oxygen_level == 0:
                diver.has_health_issue = True
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count = 0

        for d in self.divers:
            if d.has_health_issue:
                count += 1
                d.has_health_issue = False
                d.renew_oxy()
        return f"Divers recovered: {count}"

    def diver_catch_report(self, diver_name: str):
        diver = self._find_diver_by_name(diver_name)
        result = f"**{diver_name} Catch Report**"

        for f in diver.catch:
            result += f"\n{f.fish_details()}"

        return result

    def competition_statistics(self):

        result = "**Nautical Catch Challenge Statistics**"

        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        for d in sorted_divers:
            if not d.has_health_issue:
                result += f"\n{str(d)}"

        return result








