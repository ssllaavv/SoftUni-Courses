from project.equipment.base_equipment import BaseEquipment
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.base_team import BaseTeam
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam


class Tournament:

    EQUIPMENT_TYPES = ["KneePad", "ElbowPad"]
    TEAM_TYPES = ["OutdoorTeam", "IndoorTeam"]

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment = []
        self.teams = []

    def _find_team_by_name(self, name):

        team = None
        for t in self.teams:
            if t.name == name:
                team = t
                break
        return team

    def _take_last_equipment_of_a_tye(self, equipment_type):

        equipment = None
        for e in reversed(self.equipment):
            if e.__class__.__name__ == equipment_type:
                equipment = e
                break
        return equipment

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.EQUIPMENT_TYPES:
            raise Exception("Invalid equipment type!")
        equipment = eval(equipment_type)()
        self.equipment.append(equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.TEAM_TYPES:
            raise Exception("Invalid team type!")

        if self.capacity <= len(self.teams):
            return "Not enough tournament capacity."

        team = eval(team_type)(team_name, country, advantage)
        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):

        team = self._find_team_by_name(team_name)

        if team:
            equipment = self._take_last_equipment_of_a_tye(equipment_type)

            if equipment:

                if team.budget < equipment.price:
                    raise Exception("Budget is not enough!")

                else:
                    team.equipment.append(equipment)
                    team.budget -= equipment.price
                    self.equipment.remove(equipment)
                    return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):

        team = self._find_team_by_name(team_name)

        if not team:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):

        count = 0

        for e in self.equipment:
            if e.__class__.__name__ == equipment_type:
                e.increase_price()
                count += 1

        return f"Successfully changed {count}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):

        team1 = self._find_team_by_name(team_name1)
        team2 = self._find_team_by_name(team_name2)

        if not team1.__class__.__name__ == team2.__class__.__name__:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_result = team1.advantage + sum([e.protection for e in team1.equipment])
        team2_result = team2.advantage + sum([e.protection for e in team2.equipment])

        if team1_result == team2_result:
            return f"No winner in this game."

        elif team1_result > team2_result:
            team1.win()
            return f"The winner is {team1.name}."

        else:
            team2.win()
            return f"The winner is {team2.name}."

    def get_statistics(self):

        result = f"Tournament: {self.name}\nNumber of Teams: {len(self.teams)}\nTeams:"

        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        for t in sorted_teams:
            result += f"\n{t.get_statistics()}"

        return result


