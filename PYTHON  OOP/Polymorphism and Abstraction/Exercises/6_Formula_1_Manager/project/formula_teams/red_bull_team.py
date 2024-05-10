from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    EXPENSES = 250_000
    REWARDS = {1: 1_500_000, 2: 800_000, 8: 20_000, 10: 10_000}

    def calculate_revenue_after_race(self, race_pos: int):
        reward = 0
        if race_pos == 1:
            reward += 1_500_000
        elif race_pos == 2:
            reward += 800_000

        if race_pos <= 8:
            reward += 20_000
        elif race_pos <= 10:
            reward += 10_000

        revenue = reward - self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"

