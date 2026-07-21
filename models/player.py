class Player:
    def __init__(
        self,
        name,
        age,
        position,
        overall,
        potential,
        value,
        wage
    ):
        self.name = name
        self.age = age
        self.position = position
        self.overall = overall
        self.potential = potential
        self.value = value
        self.wage = wage

        self.morale = 75
        self.fitness = 100
        self.form = 75

        self.goals = 0
        self.assists = 0
        self.matches = 0

    def improve(self):
        if self.age <= 23 and self.overall < self.potential:
            self.overall += 1

    def age_up(self):
        self.age += 1

    def play_match(self):
        self.matches += 1

    def score_goal(self):
        self.goals += 1

    def get_market_value(self):
        return self.value
