from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    def __init__(self):
        self.red_bull_team= None
        self.mercedes_team = None

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name == "Red Bull":
            t = RedBullTeam(budget)
            self.red_bull_team = t
            return f"{ team_name } has joined the new F1 season."
        elif team_name == "Mercedes":
            t = MercedesTeam(budget)
            self.mercedes_team = t
            return f"{team_name} has joined the new F1 season."
        else:
            raise ValueError("Invalid team name!")

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.red_bull_team or not self.mercedes_team:
            raise "Not all teams have registered for the season."
        else:
            better_team = "Mercedes" if mercedes_pos < red_bull_pos else "Red Bull"
            message = f"Red Bull: { self.red_bull_team. calculate_revenue_after_race(red_bull_pos) }. " \
                      f"Mercedes: { self.mercedes_team.calculate_revenue_after_race(mercedes_pos) }. " \
                      f"{ better_team } is ahead at the { race_name } race."
        return message





