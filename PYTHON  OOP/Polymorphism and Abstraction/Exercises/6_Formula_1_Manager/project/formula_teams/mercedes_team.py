from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    EXPENSES = 200_000
    REWARDS = {1: 1_000_000, 3: 500_000, 5: 100_000, 7: 50_000}

    def calculate_revenue_after_race(self, race_pos: int):
        reward = 0
        if race_pos == 1:
            reward += 1_000_000
        elif race_pos <= 3:
            reward += 500_000

        if race_pos <= 5:
            reward += 100_000
        elif race_pos <= 7:
            reward += 50_000

        revenue = reward - self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is { revenue }$. Current budget { self.budget }$"