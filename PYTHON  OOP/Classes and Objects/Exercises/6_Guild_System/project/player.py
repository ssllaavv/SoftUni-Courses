class Player:
    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.guild = "Unaffiliated"
        self.skills = {}

    def add_skill(self, skill_name: str, mana_cost: int):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        skills_string = '\n'.join([f"==={skill} - {mana}" for skill, mana in self.skills.items()])
        result = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}" + "\n" + skills_string + "\n"
        return result
